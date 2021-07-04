# cook your dish here
t = int(input())
for _ in range(t):
    number  =  int(input())
    reverse = 0
    while number>0:
        last_digit = number % 10
        reverse = (reverse * 10) + last_digit
        number = int(number / 10)
    print(reverse)