class Adjnode:
    def __init__(self):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self,V):
        self.vertex = V
        self.graph = [None]*V
        print(self.graph)

    def add_edge(self,src,dest):
        node = Adjnode(dest)



g1 = Graph(4)