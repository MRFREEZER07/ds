import hashllib
class hash_map:
    def __init__(self,key,value):
        self.data=value
        self.hash=hashlib.md5(key)
        print(self.hash)
        print(self.data)
    
hash_map(1,2)