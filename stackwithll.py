class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Stack:
    def __init__(self):
        self.top=None
        self.bottom=None
        self.length =0
        
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
        
    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top=new_node
            self.bottom=new_node
        else:
            new_node.next=self.top
            self.top=new_node
            
        self.length +=1
            
    def pop(self):
        if self.top ==None:
            print("STACK IS EMPTY")
        else:
            unwanted_node=self.top
            self.top=self.top.next
            self.length -=1
            
    def print(self):
        if self.top==None :
            print("stack is empty")
        else:
            current =self.top
            while (current):
                print(current.data)
                current=current.next
                
    
        
    
    
    
s=Stack()
s.push(2)
s.push(12)
s.push(22)                      
#s.pop()
print(s.peek())
s.print()