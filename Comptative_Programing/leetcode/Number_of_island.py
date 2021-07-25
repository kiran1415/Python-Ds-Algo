from queue import PriorityQueue

q1 = PriorityQueue()

q1.put(5)
q1.put(9)
q1.put(10)
q1.put(2)
while q1:
    ele=q1.get()
    print(ele)
