from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,src,dest):
        self.graph[src].append(dest)

    def dfs(self,src):
        visited = [False] * (max(self.graph)+1)
        stack = []
        stack.append(src)
        while stack:
            top = stack.pop()
            visited[top] = True
            print(top)
            for nbr in self.graph[top]:
                if visited[nbr] == False:
                    stack.append(nbr)
                    visited[nbr] = True







g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
 
print("Following is DFS from (starting from vertex 2)")
g.dfs(2)