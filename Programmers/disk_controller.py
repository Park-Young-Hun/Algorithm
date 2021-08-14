import heapq


def solution(jobs):
    answer = 0
    time = 0
    jobs_len = len(jobs)

    jobs.sort(key=lambda x: (x[1], x[0]))  # 작업 소요시간 순으로 정렬하고 같으면 도착 시간순으로 정렬.

    while len(jobs) != 0:

        for i in range(len(jobs)):
            if jobs[i][0] <= time:  # 현재 시각 기준 도착해있는 것들 중 가장 소요시간 짧은거(이미 정렬됨) 선택해서 처리.
                answer += (time - jobs[i][0] + jobs[i][1])  # 총 작업시간 계산해서 저장.
                time += jobs[i][1]  # 선택한 작업 반영하여 현재 시각 초기화.
                jobs.remove(jobs[i])
                break
            if i == len(jobs) - 1:  # 현재 시각 기준 도착한 작업이 없으면 1초 대기.
                time += 1

    answer = answer // jobs_len

    return answer
