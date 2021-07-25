# cook your dish here
t  = int(input())
for i in range(t):
    g, c = map(int,input().split())  
    print(int(c**2/(2*g)))