class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
        
class dlinkedlist:
    def __init__(self):
        self.head=None
        self.tail=self.head
        self.length=0
        
    def print(self):
        if self.head is None:
            print('ll is empty')
        else:
            temp =self.head
            while temp != None:
                print(temp.data,end='-> ')
                
                temp=temp.next
            print("\n")    
    def prepend(self,data):
        new_node =Node(data)
        if self.head is None:
            self.head=new_node
            new_node.data=data
            self.tail=self.head
            self.length+=1
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            self.length+=1
            
    def append(self,data):
        new_node=Node(data)
        if self.head == None:
            self.head=new_node
            self.tail=self.head
            self.length+=1
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
            self.length+=1
            
    def insert(self,index,data):
        if(index>=self.length):
            print("index does not exist")
        elif( index==0):
            return self.pretend(data)
        else:
            new_node =Node(data)
            previous_node = self.head   
            
            for i in range(index-1):
                previous_node = previous_node.next
                        
            adutha_node =previous_node.next
            previous_node.next=new_node
            new_node.prev=previous_node
            new_node.next=adutha_node
            adutha_node.prev=new_node 
            self.length+=1
    
    def removebyindex(self,index):
        if(index>=self.length):
            print("index does not exist")
            print("available index " + str(self.length)) 
        elif(index==0):
            print("ll is empty")
        else:
            previous_node=self.head
            for i in range(index-1):
                previous_node=previous_node.next
            
            unwanted_node=previous_node.next
            adutha_node=previous_node.next.next
            adutha_node.prev=previous_node
            previous_node.next=adutha_node
            self.length -1
            self.print()
            
    def removebyvalue(self,value):
        if self.head is None:
            print("ll is empty")
            
        else:
            current_node=self.head
            for i in range(self.length):
                current_node=current_node.next
                if(current_node.data==value):
                    unwanted_node=current_node
                    previous_node=current_node.prev
                    adutha_node=current_node.next
                    break
                
            previous_node.next=adutha_node
            adutha_node.prev=previous_node
            self.length -1
            self.print()
    
    # def reverse(self):
    #     current_node=self.tail
    #     for i in range(self.length):
    #         current_node=current_node.prev
    #         s
    
       
l=dlinkedlist()
l.prepend(2)
l.append(2322)
l.prepend(112)
l.prepend(22)
l.append(23)
l.append(21)
#l.print()
#l.removebyindex(4)
#l.removebyvalue(2322)
l.reverse()
l.insert(3,4)

