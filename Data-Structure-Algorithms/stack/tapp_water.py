heights = [0,1,0,2,1,0,1,3,2,1,2,1]

def tappwater(heights):
    n = len(heights)
    st = []
    lm = [0] * n
    rm = [0] * n
    lm[0] = heights[0] 
    for i in range(1, n):
        lm[i] = max(lm[i-1], heights[i])
    
    rm[n-1] = heights[n-1] 
    for i in range(n-2,-1,-1):
        rm[i] = max(rm[i+1], heights[i])

    bound_water = []

    for i in range(n):
        bound_water.append(min(rm[i], lm[i]))


    water = []
    for i in range(n):
        water.append(bound_water[i] - heights[i])

    tapp_water = 0
    for i in range(n):
        tapp_water+=water[i]
    return tapp_water











print(tappwater(heights))



