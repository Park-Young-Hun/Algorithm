from queue import Queue


def solution(progresses, speeds):
    answer = []

    q = Queue()  # 각각의 기능에 대한 작업소요일을 queue에 넣음.
    for i in range(len(progresses)):
        progresses[i] = 100 - progresses[i]
        if progresses[i] % speeds[i] == 0:
            q.put(progresses[i] // speeds[i])
        else:
            q.put(progresses[i] // speeds[i] + 1)

    count = 0
    first = q.get()  # 첫번째 요소
    count += 1
    if q.empty():  # queue에 요소가 하나밖에 없을 경우.
        answer.append(1)
        return answer

    while not q.empty():

        second = q.get()  # 첫번째 요소와 비교할 비교대상 추가
        count += 1

        if first < second:  # first까지만 묶어서 배포진행.
            count -= 1  # second 제외
            answer.append(count)  # 배포
            count = 0  # 기능 갯수 초기화
            first = second  # second를 first로 초기화
            count += 1  # 새로 초기화된 first 요소 카운팅

    answer.append(count)  # 마지막 남은 기능 배포
    return answer
