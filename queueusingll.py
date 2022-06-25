class Node:
    def __init__(self,data):
        self.data= data
        self.next =None
        
class queue:
    def __init__(self):
        self.first=None
        self.last=None
        self.length=0
        
    def enqueue(self,data):
        new_node=Node(data)
        if self.first is None:
            self.first =new_node
            self.last=self.first
                        
        else:
            self.last.next =new_node
            self.last=new_node
        
        self.length +=1
    
    def dequeue(self):
        if self.first is None:
            print("queue is empty")
        elif self.first==self.last:
            self.first=None
            self.last=None
        else:
            self.first=self.first.next
        
        self.length =-1    
            
    def print(self):
        if self.first is None:
            print("queue is emoty")
        else:
            temp =self.first
            while(temp):
                print(temp.data)
                temp=temp.next
                
        
    def peek(self):
        if self.first is None:
            return None
        else:
            print (self.first.data)
    
q=queue()
q.enqueue(2)
q.enqueue(222)
q.enqueue(112)
q.peek()
q.print()