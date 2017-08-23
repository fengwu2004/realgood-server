from RequestBaseManager import RequestBaseManager
import json
import storemgr

class SaveRecommond(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        data = json.loads(self.request.body.decode('utf-8'))

        storemgr.intance().saveToDb(data)

        consultor = data['consultor']
        
        items = storemgr.intance().findInfoWith({'consultor':consultor})
        
        result = []
        
        for item in items:
            
            result.append(item)
            
            if len(result) >= 5:
                
                break
        
        self.write({'response': result})