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
        rank_wait_times[rank] += time - arrived_time

        if time < arrived_time:
            time += arrived_time - time

        while time < arrived_time + run_time:
            if ready_q and ready_q[0][1] == time:
                target = ready_q.popleft()
                heapq.heappush(wait_q, (target[1], target[0], target[2]))
            time += 1
        print(time)

        if wait_q:
            next_job = heapq.heappop(wait_q)
            arrived_time, rank, run_time = next_job
            ready_q.appendleft((rank, arrived_time, run_time))

    answer[0] = time

    for i in range(1, 11):
        answer[i] = rank_wait_times[i]

    return answer
