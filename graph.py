class graph:
    def __init__(self):
        self.number_of_nodes =0
        self.adjacent_list= {}
        
    def addVertex(self,node):
        if node not in self.adjacent_list:
            self.adjacent_list[node]=[]
            self.number_of_nodes+=1
            
    def addEdge(self,node1,node2):
        
        if node1 not in self.adjacent_list[node2]:
            self.adjacent_list[node1].append(node2)
            self.adjacent_list[node2].append(node1)
        else:
            return "connection already exist"
        
    def show_conection(self):
        print(self.adjacent_list)

myGraph = graph()
myGraph.addVertex(0)
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.addVertex(3)
myGraph.addVertex(4)
myGraph.addVertex(5)
myGraph.addVertex(6)
myGraph.addEdge(3, 1)
myGraph.addEdge(3, 4)
myGraph.addEdge(4, 2)
myGraph.addEdge(4, 5)
myGraph.addEdge(1, 2)
myGraph.addEdge(1, 0)
myGraph.addEdge(0, 2)
myGraph.addEdge(6, 5)

myGraph.show_conection()