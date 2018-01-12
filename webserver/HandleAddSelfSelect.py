import json

from data.databasemgr import DatabaseMgr
from data.storemgr import StockMgr
from data.suggest_manager import SuggestMgr
from stockmgr.consultor_score_manager import ConsultorScoreManager
from webserver.RequestBaseManager import RequestBaseManager

class HandleAddSelfSelectRequest(RequestBaseManager):
    
    def post (self, *args, **kwargs):

        data = json.loads(self.request.body.decode('utf-8'))

        stockid = data['stockId']

        add = data['add']

        DatabaseMgr.instance().selfselect.remove({'stockid': stockid})

        if add == 1:

            DatabaseMgr.instance().selfselect.insert_one({'stockid':stockid})

        self.write({'success': 1})