def solution(numbers, hand):
    answer = ''

    key_pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left_side = [1, 4, 7]
    right_side = [3, 6, 9]
    center = [2, 5, 8, 0]

    left = [3, 0]
    right = [3, 2]

    for num in numbers:
        if num in left_side:
            answer += 'L'
            left = [left_side.index(num), 0]
        elif num in right_side:
            answer += 'R'
            right = [right_side.index(num), 2]
        else:
            target = [center.index(num), 1]
            l_distance = abs(target[0] - left[0]) + abs(target[1] - left[1])
            r_distance = abs(target[0] - right[0]) + abs(target[1] - right[1])

            if l_distance > r_distance:
                answer += 'R'
                right = target
            elif l_distance < r_distance:
                answer += 'L'
                left = target
            else:
                if hand == "left":
                    answer += 'L'
                    left = target
                else:
                    answer += 'R'
                    right = target
    return answer
