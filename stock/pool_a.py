from data.stock_info import SuggestStock
from data.stock_unit import Stock
from typing import Dict, List
from datetime import datetime
from data.stock_info import PoolStock

# 精选股票池
# 存活时间策略：关注进来池中，存活时间为20天，如果有新关注，存活时间加上10天，到期移除
# 排序策略：
# a:是否是持仓股票，是，权重20
# b:关注次数，关注次数2(20),3(30),4(35),40
# c:单日较大涨幅，5%
class PoolA(object):
    
    def __init__(self):

        self.stocks = []
    
    # 每天运行一遍，检查池中的股票
    # 1：股票到达止损点，从池中清除
    # 2：股票已经达到期望涨幅，且又没有新的关注进来
    # 3：
    #
    def run(self, dt:datetime):
        
        for poolstock in self.stocks:
        
            if poolstock.checkDie(datetime):
            
                poolstock.living = False
                
                poolstock.updateConsultorScore(dt)
        
        self.sortStocks()

    def removeDeathSuggest(self):

        pass
    
    def sortStocks(self):

        self.removeDeathSuggest()

        pass
    
    def display(self):
        
        pass
    
    def retivePoolStock(self, suggest:SuggestStock) -> PoolStock:
        
        for poolstock in self.stocks:
            
            if poolstock.stockId == suggest.stockId:
                
                return poolstock
            
        poolstock = PoolStock()

        poolstock.stockId = suggest.stockId

        poolstock.addedDate = suggest.date

        poolstock.live = 20

        self.stocks.append(poolstock)
        
        return poolstock

    def addSuggest(self, suggest:SuggestStock):
    
        poolstock = self.retivePoolStock(suggest.stockId)

        poolstock.addSuggest(suggest)

