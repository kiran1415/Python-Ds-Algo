import heapq
from collections import defaultdict

def shortest_path(graph,src,dest):
    h = []
    heapq.heappush(h,(0,src))
    while len(h) != 0:
        c_cost,c_vertx = heapq.heappop(h)
        if c_vertx == dest:
            print("distance beetween {} and {}  is {}".format(src, dest,c_cost))
            return
        for neight , neighcost in graph[c_vertx]:
            heapq.heappush(h,(c_cost+neighcost,neight))  


graph = defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    u,v,w = map(str,input().split())
    graph[u].append((v,int(w)))

src,dest = map(str,input().split())
shortest_path(graph,src,dest)


