nums = [3,1,4,2]
def find132pattern(heights):
    small_right = [-1] * len(heights)
    big_right = [-1] * len(heights)
    st = []
    for i in range(len(heights)):
        while st and heights[st[-1]] >= heights[i]:
            st.pop()
        
        if st:
            small_right[i] = st[-1]
        st.append(i)
    print(small_right)
    st.clear()
    for i in range(len(heights)):
        while st and heights[st[-1]] <= heights[i]:
            st.pop()
        
        if st:
            big_right[i] = st[-1]
        st.append(i)
    print(big_right)


find132pattern(nums)