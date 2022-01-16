def solution(board, moves):
    answer = 0
    stack = []
    n = len(board)

    for move in moves:
        for i in range(n):
            item = board[i][move - 1]  # 현재 집게가 가리키는 item.

            if item != 0:  # 집게가 인형에 도달했을 경우.
                board[i][move - 1] = 0  # 인형을 뽑아주고

                if stack:  # 바구니에 이전에 담긴 인형이 있으면
                    ex_item = stack.pop()
                    if item == ex_item:  # 같은 종류 인형인지 비교.
                        answer += 2
                    else:  # 다르면 둘 다 순서대로 다시 넣어줌.
                        stack.extend([ex_item, item])
                else:
                    stack.append(item)
                break
    return answer
