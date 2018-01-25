class SuggestInfo(object):
    def __init__ (self):
        
        self.counts = [1, 1.1, 2, 3, 4, 5]
        
        self.trends = [10, 20, 30, 40]
    
    def toJson (self):
        return {'counts': self.counts, 'trends': self.trends}
    
    @classmethod
    def fromJson (cls, jsonvalue):
        
        obj = SuggestInfo()
        
        obj.counts = jsonvalue['counts']
        
        obj.trends = jsonvalue['trends']
        
        return obj
        
# item = SuggestInfo()



# print(str(item.toJson()))

import math

print(math.pow(1.3, 6))