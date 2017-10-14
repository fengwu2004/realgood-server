
from data import storemgr
from data.suggest import Consultor
from datetime import datetime
from functools import reduce

_instance = None

class AnalyseSettingManager(object):

    def __init__(self):

        pass

    @classmethod
    def instance(cls):

        global _instance

        if _instance is None:

            _instance = AnalyseSettingManager()

        return _instance


    def getStockWeight(self, stockId:str) -> int:

        return 0

    def getPredayIncreaseWeight(self, stockId:str, day:datetime) -> int:

        return 0
