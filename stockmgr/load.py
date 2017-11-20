import time
from data.stock import Stock, DayValue

def getLines(file):

    lines = [line.rstrip('\n') for line in open(file, 'r+', encoding='utf-8')]

    lines.pop(1)

    lines.pop()
    
    return lines

def getTime(value):
    
    return time.strptime(value, '%Y/%m/%d')

def formatData(lines):
    
    stock = Stock()
    
    if len(lines) > 1:
        
        values = lines[0].split(' ')
        
        stock.id = values[0]
        
        i = 1
        
        while values[i] != '日线':
        
            stock.name += values[i]
            
            i += 1
        
        lines.pop(0)

    if len(lines) <= 1:
        
        return stock
    
    for line in lines:
        
        dayvalue = DayValue()
    
        values = line.split('\t')

        if getTime(values[0]) < time.strptime('2017/1/01', '%Y/%m/%d'):
            
            continue

        dayvalue.date = values[0]

        dayvalue.open = float(values[1])

        dayvalue.max = float(values[2])

        dayvalue.min = float(values[3])

        dayvalue.close = float(values[4])

        dayvalue.tradeamount = float(values[5])

        dayvalue.tradevolume = float(values[6])

        stock.dayvalues.append(dayvalue)
        
    return stock