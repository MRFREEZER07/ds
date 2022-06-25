class Node :
    def __init__(self,data):
        self.data =data
        self.left =None
        self.right=None
        
class BST:
    def init(self):
        self.root =None
        self.number_of_nodes =0
        
        
    def insert(self,data):
        new_node = Node(data)
        if self.root == None:
            self.root =new_node
            self.number_of_nodes +=1
        else:
            current_node = self.root
            while(current_node.left != new_node) and (current_node.right != new_node):
                if new_node.data > current_node.data:
                    if current_node.right == None:
                        current_node.right = new_node
                    else:
                        current_node =current_node.right
                        
                elif new_node.data < current_node.data:
                    if current_node.left ==None:
                        current_node.left = new_node
                    else:
                        current_node =current_node.left
            self.number_of_nodes +=1
            return 
        
    def search(self,element):
        if self.root ==None:
            return "tree is empty"
        else:
            current_node=self.root
            while True:
                if current_node ==None:
                    print("elemetn not found")
                    
                if current_node.data == element:
                    return "element found"
                
                elif current_node.data < element:
                    current_node=current_node.left
                    
                elif current_node.data > element:
                    current_node=current_node.right
                    
                    
    #def remove(self,data):
        
        
bst =BST()
bst.insert(1)
bst.insert(551)
bst.insert(51)
bst.insert(19)
bst.insert(122)
bst.insert(12)
