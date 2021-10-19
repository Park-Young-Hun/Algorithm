def solution(record):
    answer = []
    dic = {}

    for i in record:
        command = i.split()  # 명령어를 분리.

        if command[0] == "Enter":
            answer.append(User(command[1], command[2], "들어왔습니다."))  # 메시지 추가.
            dic[command[1]] = command[2]  # 해당 user_id의 nickname을 초기화.
        elif command[0] == "Leave":
            answer.append(User(command[1], dic[command[1]], "나갔습니다."))  # 메시지 추가.
        else:
            dic[command[1]] = command[2]  # 해당 user_id의 nickname을 초기화.

    for i in answer:  # 한번 순회하면서 최종 nickname으로 초기화.
        i.nickname = dic[i.user_id]

    return list(map(str, answer))


class User:

    def __init__(self, user_id, nickname, act):
        self.user_id = user_id
        self.nickname = nickname
        self.act = act

    def __str__(self):
        return str(self.nickname) + "님이 " + str(self.act)

