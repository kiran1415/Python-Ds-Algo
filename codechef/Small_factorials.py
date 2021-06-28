# cook your dish here
    
def recursion(n):
    if n == 1 or n==0:
        return n 
    return n*recursion(n-1)

t = int(input())
for _ in range(t):
    num = int(input())
    ans = recursion(num)
    print(ans)

    
    