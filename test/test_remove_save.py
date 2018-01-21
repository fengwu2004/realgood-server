from data.storemgr import *
from data.suggest import Suggest
from data.databasemgr import DatabaseMgr

suggests = loadSuggests()

def doS(suggest):

    suggest.date = datetime.strptime(suggest.date, '%Y/%m/%d').strftime('%Y/%m/%d')

    return suggest

items = list(map(doS, suggests))

results = set()

for item in items:

    results.add(item)

DatabaseMgr.instance().suggests.remove({})

DatabaseMgr.instance().suggests.insert_many(list(map(lambda suggest: suggest.toJson(), results)))



