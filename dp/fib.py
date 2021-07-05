def fid(n):
    dp = [0,1]
    for i in range(1,n,1):
        print(dp)
        print(i)
        dp.append(dp[i-1]+dp[i-2])
        print(dp)
    #print(dp)
    print(dp[n])

fid(5)