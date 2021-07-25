def reverse(x):
    ans=0
    neg = False
    if x<0:
        neg=True
        x = abs(x)
    while x!=0:
        print(x)
        rem = x%10
        ans = (ans*10) + rem
        x = int(x / 10)      
    if neg:
        ans = '-'+ans
    return ans

print(reverse(123))