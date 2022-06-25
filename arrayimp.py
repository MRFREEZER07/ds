class array:
    def __init__(self):
        self.length =1
        self.data=[]
        
    def get(self,index):
        return self.data[index]
    
    def push(self,item):
        self.data[self.length]=item 
        self.length+=1
        return self.length
        
    
    
a =array()
a.push(1)
print(a)
    
    