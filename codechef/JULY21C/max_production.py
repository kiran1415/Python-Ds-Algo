# cook your dish here
t = int(input())

for i in range(t):
    d, x, y, z = map(int, input().split())
    print(max(7*x , d*y+z*(7-d)))