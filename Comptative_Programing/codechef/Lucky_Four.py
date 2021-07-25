from collections import Counter

t = int(input())
for _ in range(t):
    n = input()
    c = Counter(n)
    print(c['4'])
