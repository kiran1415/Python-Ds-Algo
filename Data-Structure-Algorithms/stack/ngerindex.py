arr = [4, 5, 2, 10, 8]


def ngetright(arr):
    n = len(arr)
    op = [-1] * n
    st = []


    for i in range(n-1,-1,-1):
        while st and arr[st[-1]] >= arr[i]:
            st.pop()

        if st:
            op[i] = st[-1]
        st.append(i)
    return op

print(ngetright(arr))