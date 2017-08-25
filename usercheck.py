import json

import tornado.web

from tokenManager import TokenManagerInstance

from RequestBaseManager import RequestBaseManager


class UserManager(RequestBaseManager):
    
    def post(self, *args, **kwargs):
        
        data = json.loads(self.request.body.decode('utf-8'))

        result = {}
        
        if self.checkValid(data):
    
            self.write({'success': '1'})
        
        else:
    
            self.write({'success': '0'})
    
    def checkValid(self, data):
    
        token = data['token']
        
        return TokenManagerInstance().checkToken(token)
    
    