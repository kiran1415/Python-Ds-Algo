# cook your dish here
t = int(input())
for i in range(t):
    a, b = map(int,input().split())  
    ans_sum = a+b
    if ans_sum < 3:
        print("1")
    elif ans_sum >=3 and ans_sum <=10:
        print("2")
    elif ans_sum >=11 and ans_sum <=60:
        print("3")
    elif ans_sum >60:
        print("4")