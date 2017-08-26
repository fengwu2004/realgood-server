from RequestBaseManager import RequestBaseManager
import json
import storemgr
import tokenManager

class SaveRecommond(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        data = json.loads(self.request.body.decode('utf-8'))
        
        token = data['token']
        
        if not tokenManager.TokenManagerInstance().checkToken(token):
        
            self.write({'response': {'success':0}})
            
            return

        storemgr.intance().saveToDb(data)

        consultor = data['consultor']
        
        items = storemgr.intance().findInfoWith({'consultor':consultor})
        
        result = []
        
        for item in items:
            
            result.append(item)
            
            if len(result) >= 5:
                
                break
                
        res = {'success':1,'data':result}
        
        self.write(res)