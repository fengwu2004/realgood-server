from tokenManager import TokenManagerInstance
from RequestBaseManager import RequestBaseManager
import json
import storemgr

class loginManager(RequestBaseManager):
    
    def options(self, *args, **kwargs):
        
        self.set_status(204)
        
        self.finish()
    
    def post(self):
        
        data = json.loads(self.request.body.decode('utf-8'))
        
        username = data['name']
        
        password = data['pwd']
        
        if storemgr.intance().checkUser(username, password):
            
            senddata = dict()

            senddata['success'] = 1

            senddata['token'] = TokenManagerInstance().createToken(username)
            
            self.write(senddata)
            
            return
        
        self.write({'success': '0'})