

class Node: #creating a node with two space like data and ref_space
    def __init__(self,data):
        self.data = data    #data
        self.next =None     #reference
        
        
class linkedlist:            #how the list is linked and other operations
    def __init__(self):
        self.head=None
        self.tail =self.head
        self.length=0 
        
    def print(self):
        if self.head == None:
            print("ll is empty")
        else:
            n=self.head
            while n!=None:
                print(n.data,"-->",end='') 
                n=n.next
            
    def append(self,data):
        new_node=Node(data)
        if self.head == None:
            self.head=new_node
            self.tail=self.head
            self.length =1
        else:
            self.tail.next = new_node
            self.tail=new_node
            self.length+=1
    
    def prepend(self,data):
        new_node=Node(data)
        if self.head == None:
            self.head=new_node
            self.tail=self.head
            self.length+=1
        else:
            new_node.next = self.head
            self.head=new_node
            self.length+=1
            
 
    def insert(self,index,data):
        if(index>=self.length):
            print("index does not exist")
            print("available index " + str(self.length))        
        elif (index==0):
            return self.prepend(data)
        else:
            new_node = Node(data)
            previous_node = self.head
            
            for i in range(index-1):
                previous_node=previous_node.next
            
            adutha_node =previous_node.next
            new_node.data=data
            new_node.next=adutha_node
            previous_node.next=new_node
            self.length+=1
            self.print()
            
    def remove(self,index):
        if(index>=self.length):
            print("index does not exist")
            print("available index " + str(self.length)) 
        elif(index==0):
            print("list is empty")
        else:
            previous_node = self.head
            for i in range(index-1):
                previous_node.next=previous_node.next
                
            unwanted_node = previous_node.next
            adutha_node =previous_node.next.next
            previous_node.next=adutha_node
            self.length -1
            self.print()
                
            
            
    
    
    
    
l =linkedlist()

l.append(2)
l.append(11)

l.prepend(3)
l.append(13)
l.insert(2,123)
print('\n')
l.remove(2)
  