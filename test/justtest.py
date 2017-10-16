from data.databasemgr import DatabaseMgr
from stock.consultor_manager import ConsultorManager
from data.suggest import Suggest

items = DatabaseMgr.instance().suggests.find({}, {'_id':0})

print(items)

results = []

for item in items:

    suggest = Suggest()

    c = ConsultorManager.instance().retriveConsultor(item['name'].strip(), item['company'].strip())

    suggest.consultorId = c.id

    suggest.stockId = item['stockId']

    suggest.stockName = item['stockName']

    suggest.date = item['date']

    results.append(suggest)

# DatabaseMgr.instance().suggestscopy.insert_many(list(map(lambda suggest: suggest.toJson(), results)))