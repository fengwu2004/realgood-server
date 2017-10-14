from collections import defaultdict
from data.suggest import *
from data import storemgr

_instance = None

class ConsultorManager(object):

    @classmethod
    def instance(cls):

        global _instance

        if _instance is None:

            _instance = ConsultorManager()

        return _instance

    def __init__(self):

        self.consltors = []

    def loadFromDB(self):

        pass

    def retriveConsultor(self, name:str, company:str) -> Consultor:

        for consultor in self.consltors:

            if consultor.name == name and consultor.company == company:

                return consultor.id

        consultor = Consultor(len(self.consltors), name, company)

        self.consltors.append(consultor)

        return consultor


