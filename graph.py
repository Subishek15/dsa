
class Graph:
    def __init__(self):
        self.graph={}
        self.directed=False

    def addVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def addEdges(self,src,dest):
        self.addVertex(src)
        self.addVertex(dest)

        self.graph[src].append(dest)
        if not self.directed:
            self.graph[dest].append(src)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}->{self.graph[vertex]}")

g=Graph()
g.addEdges('A','B')
g.addEdges('A','C')
g.addEdges('B','C')
g.addEdges('C','D')
g.display()
