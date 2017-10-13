from typing import List
from collections import defaultdict
from data.suggest import SuggestScore, Suggest, Consultor
from openpyxl import load_workbook


_ratesettings = []

_instance = None

class RateSetting(object):

    def __init__(self, start, end, score):

        self.start = start

        self.end = end

        self.score = score

def initRateSetting() -> List[RateSetting]:

    global _ratesettings

    if len(_ratesettings) != 0:

        return _ratesettings

    wb = load_workbook('./ratesetting.xlsx')

    ws = wb.active

    for i in range(2, ws.max_row + 1):

        rs = RateSetting(ws['A' + str(i)].value, ws['B' + str(i)].value, ws['C' + str(i)].value)

        _ratesettings.append(rs)

    return _ratesettings

def retriveConsulterRate(v0:float, vMax:float) -> int:

    vMaxPercent = (vMax - v0) * 100 / v0

    items = initRateSetting()

    for item in items:

        if item.start <= vMaxPercent <= item.end:

            return item.score

    return 0

class ConsultorScoreManager(object):

        @classmethod
        def instance(cls):

            global _instance

            if _instance is None:

                _instance = ConsultorScoreManager()

            return _instance

        def __init__(self):

            self.consultorscores = defaultdict(list)

        def addConsultorScore(self, score: int, suggest: Suggest):

            suggestscore = SuggestScore(score, suggest)

            self.consultorscores[suggest.consultor].append(suggestscore)

        def getScores(self, consultor: Consultor) -> [SuggestScore]:

            return self.consultorscores[consultor]

        def saveToDB(self):

            pass

        def loadFromDB(self):

            pass