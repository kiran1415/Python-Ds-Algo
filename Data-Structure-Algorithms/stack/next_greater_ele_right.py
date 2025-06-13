lst = [1,3,4,1,3,5,4,6,1,2,7,9,3,5]

def nge(arr):
    l  = len(arr)
    op = [-1] * l
    st = []
    for i in range(len(arr)-1, -1, -1):
        while st and st[-1] <= arr[i]:
            st.pop()

        if st:
            op[i] = st[-1]
        st.append(arr[i])
    return op

print(nge(lst))

