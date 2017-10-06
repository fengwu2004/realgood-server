from data.stock_info import SuggestStock
from data.stock_unit import Stock
from typing import Dict

# 股票池
# 策略：
# 1：选定一个起始日期，超过60天，运行至当前日，找出最终在股票池中的股票
class PoolA(object):
    
    def __init__(self):

        self.stocks = Dict[str, SuggestStock]
    
    def run(self):
        
        pass
    
    def display(self):
        
        pass
    
    def checkEnableAdd(self, suggest:SuggestStock):
        
        if suggest.stockId in self.stocks:
            
            preSuggest = self.stocks[suggest.stockId]
            
            
        
        return True

    def checkEnableRemove(self, suggest: SuggestStock):
        
        return True
    
    def addSuggest(self, suggest:SuggestStock):
        
        pass
    
    def removeSuggest(self, suggest:SuggestStock):
        
        pass

    