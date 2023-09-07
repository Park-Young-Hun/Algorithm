import heapq
from collections import defaultdict, deque


def solution(program):
    answer = [0] * 11
    rank_wait_times = defaultdict(int)

    program.sort(key=lambda x: (x[1], x[0]))
    ready_q = deque(program)
    wait_q = []

    time = 0

    while ready_q:
        rank, arrived_time, run_time = ready_q.popleft()

        if time < arrived_time:
            time += arrived_time - time

        rank_wait_times[rank] += time - arrived_time

        time += run_time

        while ready_q and ready_q[0][1] <= time:
            heapq.heappush(wait_q, ready_q.popleft())

        if wait_q:
            next_job = heapq.heappop(wait_q)
            ready_q.appendleft(next_job)

    answer[0] = time

    for i in range(1, 11):
        answer[i] = rank_wait_times[i]

    return answer
