# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    last_digit = n % 10
    first = n 
    while(first>=10):
        first = int(first/10)
    print(first+last_digit)        