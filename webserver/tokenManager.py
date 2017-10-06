import jwt

secretKey = 'jsdjfiofjenwkdsjlskjslkdfjsdlfk'

class TokenManager(object):
    
    def __init__(self):
    
        self.count = 0
        
        self.tokens = []
        
    def checkToken(self, token):
        
        try:
            dc = jwt.decode(token, secretKey, algorithms = ['HS256'])
        except:
            return False
        
        print(dc)
        
        return True
    
    def createToken(self, userName):
        
        token = jwt.encode({'user': userName}, secretKey, algorithm = 'HS256').decode('utf-8')

        return token

__intance = 0

def instance():
    
    global __intance
    
    if __intance == 0:

        __intance = TokenManager()

    return __intance