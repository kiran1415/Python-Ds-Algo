import heapq
from collections import defaultdict



lst = [[25,2,4],[4,1,2],[5,1,3],[10,1,4],[9,3,4]]

heapq.heapify(lst)
while len(lst)>0:
    print(heapq.heappop(lst))




