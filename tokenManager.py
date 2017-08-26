from jwt import JWT

secretKey = 'jsdjfiofjenwkdsjlskjslkdfjsdlfk'

class TokenManager(object):
    
    def __init__(self):
    
        self.count = 0
        
        self.tokens = []
        
    def checkToken(self, token):
        
        dc = JWT.decode(token, secretKey, algorithms=['HS256'])
        
        print(dc)
        
        return True
    
    def removeInvalidToken(self, userName):
    
        for tokenset in self.tokens:
        
            if userName in tokenset:
                
                self.tokens.remove(tokenset)
                
                return
    
    def createToken(self, userName):
        
        token = JWT.encode({'user': userName}, secretKey + userName, algorithm = 'HS256').decode('utf-8')

        return token

__intance = 0

def TokenManagerInstance():
    
    global __intance
    
    if __intance == 0:

        __intance = TokenManager()

    return __intance