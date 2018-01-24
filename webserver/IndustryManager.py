import json

from data import storemgr
from data.databasemgr import DatabaseMgr
from webserver.RequestBaseManager import RequestBaseManager
from webserver import tokenManager


class IndustryManager(RequestBaseManager):
    
    def post(self):
        
        items = DatabaseMgr.instance().industry.find({}, {'_id':0})

        results = [item['firstindustry'] for item in items]

        senddata = dict()

        senddata['success'] = 1

        senddata['data'] = list(results)

        self.write(senddata)