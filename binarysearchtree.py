from tkinter import N


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
        
class bst:
    def __init__(self):
        self.root=None
        self.number_of_nodes=0
        
    def insert(self,data):
        new_node=Node(data)
        if self.root is None:
            self.root=new_node
            self.number_of_nodes+=1
        else:
            current_node=self.root
            while True: #until new_node become left or right
                if new_node.data<current_node.data:
                    if current_node.left ==None:
                        current_node.left=new_node
                    else:
                        current_node=current_node.left
                elif new_node.data>current_node.data:
                    if current_node.right ==None:
                        current_node.right=new_node
                    else:
                        current_node=current_node.right
                else:
                    break       
            self.number_of_nodes +=1
            return
    
    
    def search(self,data):
        if self.root == None:
            return "Tree Is Empty"
        else:
            current_node = self.root
            while (current_node):
                if current_node == None:
                    return "Not Found"
                elif current_node.data == data:
                    return "Found"
                elif current_node.data > data:
                    current_node = current_node.right
                elif current_node.data < data:
                    current_node = current_node.left
            
    def remove(self, data):
        if self.root == None: #Tree is empty
            return "Tree Is Empty"
        current_node = self.root
        parent_node = None
        while current_node!=None: #Traversing the tree to reach the desired node or the end of the tree
            if current_node.data > data:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.data < data:
                parent_node = current_node
                current_node = current_node.right
            else: #Match is found. Different cases to be checked
                #Node has left child only
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return

                #Node has right child only
                elif current_node.left == None:
                    if parent_node == None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.right
                            return

                #Node has neither left nor right child
                elif current_node.left == None and current_node.right == None:
                    if parent_node == None: #Node to be deleted is root
                        current_node = None
                        return
                    if parent_node.data > current_node.data:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return

                #Node has both left and right child
                elif current_node.left != None and current_node.right != None:
                    del_node = current_node.right
                    del_node_parent = current_node.right
                    while del_node.left != None: #Loop to reach the leftmost node of the right subtree of the current node
                        del_node_parent = del_node
                        del_node = del_node.left
                    current_node.data = del_node.data #The value to be replaced is copied
                    if del_node == del_node_parent: #If the node to be deleted is the exact right child of the current node
                        current_node.right = del_node.right
                        return
                    if del_node.right == None: #If the leftmost node of the right subtree of the current node has no right subtree
                        del_node_parent.left = None
                        return
                    else: #If it has a right subtree, we simply link it to the parent of the del_node
                        del_node_parent.left = del_node.right
                        return
        return "Not Found"


    def remove(self,data):
        if self.root==None:
            print("tree is empty")
            
        current_node =self.root
        parent_node=none
        while current_node != None:
            if current_node.data >data:
                parent_node=current_node
                current_node =current_node.ri











b=bst()
b.insert(12)

b.insert(14)
b.insert(1211)
b.insert(11)
b.insert(22)
b.remove(12)
print(b)