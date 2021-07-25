def solve(n):
    if n==0:
        print("finished",n)
        return
    solve(n-1)


solve(5)