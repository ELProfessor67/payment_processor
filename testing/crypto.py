from cryptography.fernet import Fernet
from json import loads,dumps

class Cryptography:
    def __init__(self,KEY):
        self.KEY = KEY
        self.fernet = Fernet(KEY)

    
    def encrypt(self,data):
        return self.fernet.encrypt(str(data).encode())
    
    def decrypt(self,data):
        return self.fernet.decrypt(str(data).encode('utf-8')).decode()
    
    def dic(self,data):
        try:
            return loads(data)
        except Exception as e:
            return False