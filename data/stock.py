import time

class DayValue(object):

    def __init__(self):

        self.open = 0

        self.close = 0

        self.low = 0

        self.high = 0

        self.date = ''

        self.tradeamount = 0

        self.tradevolume = 0

    def isHammer(self):

        return self.isHammer_green() or self.isHammer_red()

    def isHammer_green(self):

        if self.close < self.open:

            return False

        if (self.high - self.low)/self.open < 0.06:

            return False

        if self.open - self.close != 0 and (self.open - self.low)/(self.close - self.open) < 2:

            return False

        if (self.high - self.close)/self.open > 0.01:

            return False

        return True

        pass

    def isHammer_red(self):

        if self.open < self.close:

            return False

        if (self.high - self.low)/self.open < 0.06:

            return False

        if self.open - self.close != 0 and (self.close - self.low)/(self.open - self.close) < 2:

            return False

        if (self.high - self.open)/self.open > 0.01:

            return False

        return True

    def toJson(self):

        return {
            'Open':self.open,
            'Close':self.close,
            'Low': self.low,
            'High': self.high,
            'Date': self.date,
            'tradeamount': self.tradeamount,
            'Volume': self.tradevolume,
        }

    @classmethod
    def fromJson(cls, jsonvalue):

        obj = DayValue()

        obj.open = jsonvalue['Open']

        obj.close = jsonvalue['Close']

        obj.low = jsonvalue['Low']

        obj.high = jsonvalue['High']

        obj.date = jsonvalue['Date']

        obj.tradeamount = jsonvalue['tradeamount']

        obj.tradevolume = jsonvalue['Volume']

        return obj

class Stock(object):

    def __init__ (self):

        self.id = 0

        self.name = ''

        self.dayvalues = []

    def findIndex(self, date:str):

        t0 = time.strptime(date, '%Y/%m/%d')

        index = 0

        for dayvalue in self.dayvalues:

            t = time.strptime(dayvalue.date, '%Y/%m/%d')

            if t < t0:

                index += 1
            else:

                break

        return index

    def findHeighestValue(self, date:str) -> DayValue:

        start = self.findIndex(date)

        if start >= len(self.dayvalues):

            return None

        return max(self.dayvalues[start:], key = lambda x: x.close)

    def findLowestValue(self, date:str) -> DayValue:

        start = self.findIndex(date)

        if start >= len(self.dayvalues):

            return None

        return min(self.dayvalues[start:], key = lambda x: x.low)

    def getDayValue(self, index:int) -> DayValue:

        if index < 0:

            return self.dayvalues[0]

        if index >= len(self.dayvalues):

            return self.dayvalues[len(self.dayvalues) - 1]

        return self.dayvalues[index]

    def getDayIndex(self, date:str):

        t0 = time.strptime(date, '%Y/%m/%d')

        index = 0

        for dayvalue in self.dayvalues:

            t = time.strptime(dayvalue.date, '%Y/%m/%d')

            if t < t0:

                index += 1
            else:
                break

        return index

    def toJson(self):

        dayvalues = []

        for dayvalue in self.dayvalues:

            dayvalues.append(dayvalue.toJson())

        return {
            'id':self.id,
            'name':self.name,
            'dayvalues':dayvalues
        }

        pass

    @classmethod
    def fromJson(cls, jsonvalue):

        if jsonvalue is None:

            return None

        obj = Stock()

        obj.id = jsonvalue['id']

        obj.name = jsonvalue['name']

        obj.dayvalues = []

        for item in jsonvalue['dayvalues']:

            obj.dayvalues.append(DayValue.fromJson(item))

        return obj