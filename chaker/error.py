class ChakerError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
        
class ChakerParseError(ChakerError):
    def __init__(self,msg):
        super().__init__(msg)
