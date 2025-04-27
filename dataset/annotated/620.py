def largest_rectangle_area(heights: list[int]) -> int:
    st = []
    max_area = 0
    index = 0
    while index < len(heights):
        if len(st) == 0 or heights[st[-1]] <= heights[index]:
            st.append(index)
            index += 1
        else:
            l = st.pop()
            max_area = max(max_area, heights[l] * (index if len(st) == 0 else index - st[-1] - 1))
    while len(st) > 0:
        l = st.pop()
        max_area = max(max_area, heights[l] * (index if len(st) == 0 else index - st[-1] - 1))
    return max_area

