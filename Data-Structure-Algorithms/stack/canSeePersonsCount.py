def canSeePersonsCount(heights):
    n = len(heights)
    a = [0] *n
    for i in range(n):
        count = 1
        for j in range(i+2, n):
            if heights[i] >= heights[j] and heights[j-1] < heights[j]:
                count+=1
        a[i] = count+1
    print(a)

#heights = [5,1,2,3,10]
heights = [10,6,8,5,11,9]
canSeePersonsCount(heights)