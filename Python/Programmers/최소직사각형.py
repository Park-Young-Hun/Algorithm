def solution(sizes):
    n = len(sizes)

    width = [sizes[i][0] for i in range(n)]
    height = [sizes[i][1] for i in range(n)]

    for i in range(n):
        if height[i] > width[i]:
            temp = width[i]
            width[i] = height[i]
            height[i] = temp

    return max(width) * max(height)
