from io import BytesIO
from data import storemgr
from data.suggest import Suggest, Consultor
from openpyxl import load_workbook
from stock.consultor_manager import ConsultorManager
from webserver.RequestBaseManager import RequestBaseManager

def getItems(ws) -> [Suggest]:
    
    results = []
    
    for i in range(1, ws.max_row):
    
        obj = Suggest()
        
        index = str(i + 1)
        
        temp = str(ws['A' + index].value)
        
        obj.date = temp[0:10]

        obj.stockId = ws['D' + index].value

        obj.stockName = storemgr.getStockName(obj.stockId)
        
        if obj.stockName is None:
            
            continue

        consultorName = ws['C' + index].value

        consultorCompany = ws['B' + index].value

        consultor = ConsultorManager.instance().retriveConsultor(consultorName, consultorCompany)

        obj.consultorId = consultor.id

        results.append(obj)
        
    return results

class SaveSuggestExcel(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        data = self.request.files['upload'][0].body

        wb = load_workbook(filename = BytesIO(data))
        
        ws = wb.active
        
        storemgr.saveSuggests(getItems(ws))

        self.write({'success': 1})