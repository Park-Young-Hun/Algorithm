import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)  # heap 변환.

    while scoville[0] < K:  # 가장 작은 스코빌 지수가 K이상이 될 때까지 실행.

        if len(scoville) == 1:  # 스코빌 지수가 하나만 남을 때까지 섞었는데도 K보다 작으면 -1 리턴.
            return -1

        new_scv = heapq.heappop(scoville) + heapq.heappop(scoville) * 2  # 가장 작은것,그 다음 작은것을 뽑아서 섞음.
        heapq.heappush(scoville, new_scv)  # 새로운 스코빌 지수 추가.
        answer += 1

    return answer
