"""
Given a graph and a source vertex src in graph, find shortest paths from src to all vertices in the given graph.
The graph may contain negative weight edges.We have discussed Dijkstra’s algorithm for this problem.
Dijkstra’s algorithm is a Greedy algorithm and time complexity is O(VLogV) (with the use of Fibonacci heap).
Dijkstra doesn’t work for Graphs with negative weight edges, Bellman-Ford works for such graphs. Bellman-Ford is also simpler than Dijkstra and suites well for distributed systems. 
But time complexity of Bellman-Ford is O(VE), which is more than Dijkstra.
"""

from collections import defaultdict

class Graph:
    def __init__(self,V):
        self.V = V
        self.graph = []

    def add_edge(self,src,dest,weight):
        self.graph.append([src,dest,weight])


    def bellaman_ford(self,src):
        dist = [float("Inf")]*self.V
        dist[src] = 0

        for _ in range(self.V-1):
            for src,dest,weight in self.graph:
                if dist[src]!=  float("Inf") and dist[src] + weight < dist[dest]:
                    dist[dest] = dist[src]+ weight

        print(dist)



g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)
 
# Print the solution
g.bellaman_ford(0)

