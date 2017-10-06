import tornado.web
from webserver import tokenManager
import json

class RequestBaseManager(tornado.web.RequestHandler):
    
    def set_default_headers(self):
        
        self.set_header("Access-Control-Allow-Origin", "*")
        
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        
    def checkToken(self):
        
        return True
        
        data = json.loads(self.request.body.decode('utf-8'))

        if not 'token' in data or not tokenManager.instance().checkToken(data['token']):

            return False
        
        return True