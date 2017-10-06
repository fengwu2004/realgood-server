from io import BytesIO
from data import storemgr
from data.stock_info import SuggestStock, Consultor
from openpyxl import load_workbook
from webserver.RequestBaseManager import RequestBaseManager

def getItems(ws) -> [SuggestStock]:
    
    results = []
    
    for i in range(1, ws.max_row):
    
        obj = SuggestStock()
        
        index = str(i + 1)
        
        temp = str(ws['A' + index].value)
        
        obj.date = temp[0:10]

        obj.stockId = ws['D' + index].value

        obj.stockName = storemgr.getStockName(obj.stockId)
        
        if obj.stockName is None:
            
            continue
        
        obj.consultor = Consultor.fromJson({
            'company':ws['B' + index].value,
            'name':ws['C' + index].value
        })
        
        results.append(obj)
        
    return results

class SaveRecommondExcel(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        data = self.request.files['upload'][0].body

        wb = load_workbook(filename = BytesIO(data))
        
        ws = wb.active
        
        storemgr.saveSuggests(getItems(ws))

        self.write({'success': 1})