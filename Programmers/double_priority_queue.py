import heapq


def solution(operations):
    answer = []
    heap = []

    for i in operations:
        command = i.split()
        if command[0] == 'I':
            heapq.heappush(heap, int(command[1]))
        else:
            if len(heap) == 0:
                continue

            if command[1] == '-1':
                heapq.heappop(heap)
            else:
                max_val = heap[0]
                for i in heap:
                    if max_val <= i:
                        max_val = i

                heap.remove(max_val)

            if len(heap) != 0:
                heapq.heapify(heap)

    if len(heap) == 0:
        return [0, 0]

    heap.sort()
    answer.append(heap[len(heap) - 1])
    answer.append(heap[0])

    return answer
