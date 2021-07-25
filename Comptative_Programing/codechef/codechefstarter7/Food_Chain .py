# cook your dish here
t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    count = 1
    if b>a:
        print("1")
    else:
        while a !=1:
            count+=1
            a = int(a / b)
        print(count+1)
        
            
    