import jwt

secretKey = 'jsdjfiofjenwkdsjlskjslkdfjsdlfk'

class TokenManager(object):
    
    def __init__(self):
    
        self.count = 0
        
        self.tokens = []
        
    def checkToken(self, token):
        
        dc = jwt.decode(token, secretKey, algorithms=['HS256'])
        
        print(dc)
        
        return True
    
    def removeInvalidToken(self, userName):
    
        for tokenset in self.tokens:
        
            if userName in tokenset:
                
                self.tokens.remove(tokenset)
                
                return
    
    def createToken(self, userName):
        
        token = jwt.encode({'user': userName}, secretKey + userName, algorithm = 'HS256').decode('utf-8')

        return token

__intance = 0

def TokenManagerInstance():
    
    global __intance
    
    if __intance == 0:

        __intance = TokenManager()

    return __intance