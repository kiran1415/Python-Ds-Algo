heights = [5,4,1,2]


def max_area_histogram(heights):
    small_left = [-1] * len(heights)
    small_right = [len(heights)] * len(heights)
    max_area = 0
    st = []
    for i in range(len(heights)-1, -1, -1):
        print(i)
        while st and heights[st[-1]] >= heights[i]:
            st.pop()
        
        if st:
            small_right[i] = st[-1]
        st.append(i)
    print(small_right)
    st.clear()
    for i in range(len(heights)):
        while st and heights[st[-1]] >= heights[i]:
            st.pop()
        
        if st:
            small_left[i] = st[-1]
        st.append(i)
    print(small_left)


    for i in range(len(heights)):
        width = small_right[i] - small_left[i] - 1
        area = width * heights[i]
        max_area = max(max_area, area)
    return max_area



print(max_area_histogram(heights))


