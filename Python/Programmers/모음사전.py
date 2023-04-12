from collections import defaultdict


def dfs(txt):
    alphabets = ['A', 'E', 'I', 'O', 'U']
    answer.append(txt)

    for alphabet in alphabets:
        new_txt = txt + alphabet

        if len(new_txt) > 5:
            return

        if not visited[new_txt]:
            visited[new_txt] = True
            dfs(new_txt)


def solution(word):
    global answer
    global visited
    visited = defaultdict(bool)
    answer = []
    dfs("")

    return answer.index(word)
