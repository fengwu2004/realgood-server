from data import storemgr
from stock.pool_a import PoolA

pool = PoolA()

allSuggests = storemgr.loadSuggests()

for suggest in allSuggests:
    
    if pool.checkEnableAdd(suggest):
        
        pool.addSuggest(suggest)
        
        continue
        
    if pool.checkEnableRemove(suggest):
        
        pool.removeSuggest(suggest)
        
        continue
        
pool.display()
        