class Unit(object):
    
    def __init__(self, x, y):
        
        self.x = x
        
        self.y = y
        
    def toJson(self):
        
        return self.__dict__

    @classmethod
    def fromJson(cls, jsonvalue):
        
        obj = Unit(jsonvalue['x'], jsonvalue['y'])

        return obj
        
        
class Complex(object):
    
    def __init__(self):
        
        self.a = 100
        
        self.b = 100
        
        self.unit = Unit(10, 15)
        
    def toJson(self):
        
        return {'a':self.a,'b':self.b,'unit':self.unit.toJson()}

    @classmethod
    def fromJson(cls, jsonvalue):
    
        obj = Complex()

        obj.a = jsonvalue['a']

        obj.a = jsonvalue['a']

        obj.unit = Unit.fromJson(jsonvalue['unit'])
    
        return obj

a = Complex()

c = a.toJson()

d = a.fromJson(c)

print('OK')