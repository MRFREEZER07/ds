class stack:
    def __init__(self):
        self.array = []
        
    def peek(self):
        return self.array[len(self.array)-1]
    
    def push(self,data):
        self.array.append(data)
        return 
    def pop(self):
        if len(self.array) !=0:
            self.array.pop()
            print("poped")
        else:
            print("empty staack")
            
    def print_stack(self):
        for i in range(len(self.array)):
            print(self.array[i])
            
            
s=stack()
s.push(2)
s.push(3)
s.push(12)
s.push(1111)
print("elemet :" + str(s.peek())) 
s.print_stack()