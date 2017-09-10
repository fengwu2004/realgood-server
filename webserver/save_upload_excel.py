import json
from io import BytesIO
import storemgr
from data.stock_info import SuggestStock
from webserver import tokenManager
from openpyxl import Workbook
from openpyxl import load_workbook
from webserver.RequestBaseManager import RequestBaseManager

def getItems(ws) -> [SuggestStock]:
    
    results = []
    
    for i in range(1, ws.max_row):
    
        obj = SuggestStock()
        
        index = str(i + 1)
        
        temp = ws['A' + index].value
        
        obj.date = temp[0:10]
        
        obj.company = ws['B' + index].value
        
        obj.name = ws['C' + index].value
        
        obj.stockId = ws['D' + index].value
        
        obj.stockName = storemgr.intance().getStockName(obj.stockId)

        results.append(obj)
        
    return results

class SaveRecommondExcel(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        data = self.request.files['upload'][0].body

        wb = load_workbook(filename=BytesIO(data))
        
        ws = wb.active
        
        storemgr.intance().saveSuggests(getItems(ws))

        if not tokenManager.TokenManagerInstance().checkToken(data['token']):
            
            self.write({'success': -1})
    
            return

        self.write({'success': 1})