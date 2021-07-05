from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,src,dest):
        self.graph[src].append(dest)



    def bfs(self,src):
        visited = [False] * (max(self.graph)+1)
        queue = []
        queue.append(src)
        visited[src] = True
        while queue:
            top = queue.pop(0)
            print(top)
            for i in self.graph[top]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True





g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.bfs(2)
















