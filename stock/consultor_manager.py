from collections import defaultdict
from data.suggest import *
from data import storemgr
from data.databasemgr import DatabaseMgr

_instance = None

class ConsultorManager(object):

    @classmethod
    def instance(cls):

        global _instance

        if _instance is None:

            _instance = ConsultorManager()

        return _instance

    def __init__(self):

        self.consltors = self.loadFromDB()

    def loadFromDB(self):

        items = DatabaseMgr.instance().consultors.find({}, {'_id':0})

        return list(map(lambda item: Consultor.fromJson(item), items))

    def saveToDB(self):

        items = list(map(lambda consulor: consulor.toJson(), self.consltors))

        DatabaseMgr.instance().consultors.insert_many(items)

    def retriveConsultorBy(self, consultorId:int):

        for consultor in self.consltors:

            if consultor.id == consultorId:

                return consultor

        return None

    def retriveConsultor(self, name:str, company:str) -> Consultor:

        for consultor in self.consltors:

            if consultor.name == name and consultor.company == company:

                return consultor

        consultor = Consultor(name, company, len(self.consltors))

        DatabaseMgr.instance().consultors.insert_one(consultor.toJson())

        self.consltors.append(consultor)

        return consultor