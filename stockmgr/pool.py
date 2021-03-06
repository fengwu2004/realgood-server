from collections import namedtuple
from typing import Tuple

from data import storemgr
from data.storemgr import *
from stockmgr.analyse_setting_manager import AnalyseSettingManager
from stockmgr.consultor_score_manager import retriveConsulterRate, ConsultorScoreManager
from stockmgr.retrive_trade_days import getTradeDayCount, getNextTradeDay


class PoolStock(object):
    def __init__(self):

        self.stockId = ''

        self.addedDate = ''

        self.live = 20

        self.weight = 0

        self.predayincreaseweight = 0

        self.living = True

        self.suggests = []

    def getStockWeight(self):

        return AnalyseSettingManager.instance().getStockWeight(self.stockId)

    def getPredayIncreaseWeight(self, day: datetime, adddate:datetime):

        if day < adddate:

            return 0

        return AnalyseSettingManager.instance().getPredayIncreaseWeight(self.stockId, day)

    def getConsultorWeight(self):

        return sum(list(map(lambda suggest:ConsultorScoreManager.instance().getConsultorWeight(suggest.consultorId), self.suggests)))

    def updateWeight(self, day: datetime):

        self.weight = self.getStockWeight()

        self.weight += self.getConsultorWeight()

        self.predayincreaseweight += self.getPredayIncreaseWeight(day, datetime.strptime(self.addedDate, '%Y/%m/%d'))

        self.weight += self.predayincreaseweight

    def checkDie(self, dt: datetime) -> bool:

        startdt = datetime.strptime(self.addedDate, '%Y/%m/%d')

        count = getTradeDayCount(startdt, dt)

        return count > self.live

    def addSuggest(self, suggest: Suggest):

        self.suggests.append(suggest)

        if len(self.suggests) > 1:

            self.live = 30

        self.weight += 1

    def updateConsultorScore(self, dt: datetime):

        for suggest in self.suggests:

            startdt = datetime.strptime(suggest.date, '%Y/%m/%d')

            increase = getMaxIncrease(self.stockId, startdt, dt)

            score = retriveConsulterRate(increase[0], increase[1])

            ConsultorScoreManager.instance().addConsultorScore(score, suggest)

# 精选股票池
# 存活时间策略：关注进来池中，存活时间为20天，如果有新关注，存活时间加上10天，到期移除
# 排序策略：
# a:是否是持仓股票，是，权重20
# b:关注次数，关注次数2(20),3(30),4(35),40
# c:单日较大涨幅，5%

_intance = None

class PoolA(object):
    
    def __init__(self):

        self.stocks = []

    @classmethod
    def intance(cls):

        global _intance

        if _intance is None:

            _intance = PoolA()

        return _intance
    
    # 每天运行一遍，检查池中的股票
    # 1：股票到达止损点，从池中清除
    # 2：股票已经达到期望涨幅，且又没有新的关注进来
    #
    def run(self, dt:datetime):
        
        for poolstock in self.stocks:
        
            if poolstock.checkDie(dt):
            
                poolstock.living = False
                
                poolstock.updateConsultorScore(dt)

            else:

                poolstock.updateWeight(dt)
        
        self.sortStocks()

    def doRunFrom(self, dt:str):

        self.stocks = []

        dt = getNextTradeDay(dt)

        while dt:

            dtstr = dt.strftime('%Y/%m/%d')

            print(dtstr)

            allSuggests = storemgr.loadSuggestsOfDate(dtstr)

            for suggest in allSuggests:

                self.addSuggest(suggest)

            t = datetime.now()

            self.run(dt)

            print(datetime.now() - t)

            dt = getNextTradeDay(dtstr)

        self.show()

    def getReuslt(self):

        dtstr = datetime.now().strftime('%Y/%m/%d')

        Item = namedtuple('Item', 'name adddate consultor trend total increase')

        results = []

        for poolstock in self.stocks:

            stock = getStock(poolstock.stockId)

            close0 = stock.getDayValue(stock.getDayIndex(poolstock.addedDate)).close

            close1 = stock.getDayValue(stock.getDayIndex(dtstr)).close

            predayweight = poolstock.predayincreaseweight

            consultorweight = '%.1f' % (poolstock.weight - predayweight)

            totalweight = '%.1f' % poolstock.weight

            increase = '%.1f' % ((close1 - close0) * 100 / close0)

            item = Item(name = getStockName(poolstock.stockId),
                        adddate = poolstock.addedDate,
                        consultor = consultorweight,
                        trend = predayweight,
                        total = totalweight,
                        increase = increase)

            results.append(item._asdict())

        return results

    def show(self):

        dtstr = datetime.now().strftime('%Y/%m/%d')

        for poolstock in self.stocks:

            stock = getStock(poolstock.stockId)

            close0 = stock.getDayValue(stock.getDayIndex(poolstock.addedDate)).close

            close1 = stock.getDayValue(stock.getDayIndex(dtstr)).close

            predayweight = poolstock.predayincreaseweight

            consultorweight = '%.1f' % (poolstock.weight - predayweight)

            totalweight = '%.1f' % poolstock.weight

            increase = '%.1f' % ((close1 - close0) * 100/close0)

    def removeDeathSuggest(self):

        self.stocks = list(filter(lambda x: x.living, self.stocks))

    def sortStocks(self):

        self.removeDeathSuggest()

        self.stocks.sort(key = lambda poolstock: poolstock.weight, reverse = True)

    def retivePoolStock(self, suggest:Suggest) -> PoolStock:

        if checkIsNewStock(suggest.stockId, suggest.date):

            return None

        for poolstock in self.stocks:
            
            if poolstock.stockId == suggest.stockId:
                
                return poolstock
            
        poolstock = PoolStock()

        poolstock.stockId = suggest.stockId

        poolstock.addedDate = suggest.date

        poolstock.live = 20

        self.stocks.append(poolstock)
        
        return poolstock

    def addSuggest(self, suggest:Suggest):
    
        poolstock = self.retivePoolStock(suggest)

        if poolstock:

            poolstock.addSuggest(suggest)

def getDayValues(stockId:str, dt0:datetime, dt1:datetime):

    stock = StockMgr.instance().getStock(stockId)

    if stock is None:

        return None

    resulsts = []

    for dayvalue in stock.dayvalues:

        dt = datetime.strptime(dayvalue.date, '%Y/%m/%d')

        if dt < dt0:

            continue

        if dt > dt1:

            break

        resulsts.append(dayvalue)

    return resulsts

def getMaxIncrease(stockId:str, dt0:datetime, dt1:datetime) -> Tuple[float, float, int]:

    dayvalues = getDayValues(stockId, dt0, dt1)

    if dayvalues is None or len(dayvalues) <= 1:

        return 1, 1, 1

    v0 = dayvalues[0].close

    vMax = dayvalues[0].close

    vMaxDay = 0

    index = 0

    for dayvalue in dayvalues:

        index += 1

        if dayvalue.close > vMax:

            vMax = dayvalue.close

            vMaxDay = index

    return v0, vMax, vMaxDay

