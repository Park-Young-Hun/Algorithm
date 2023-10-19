class Task:
    def __init__(self, name, start, playtime):
        self.name = name
        self.start = start
        self.playtime = playtime


def solution(plans):
    completed = []
    wait_q = []
    ready_q = []

    for name, start, playtime in plans:
        hour, minute = map(int, start.split(":"))
        start = hour * 60 + minute

        wait_q.append(Task(name, start, int(playtime)))

    wait_q.sort(key=lambda x: -x.start)

    ready_q.append(wait_q.pop())
    cur_time = ready_q[-1].start

    while ready_q or wait_q:
        if ready_q:
            task = ready_q.pop()
        else:
            task = wait_q.pop()
            cur_time = task.start

        if not wait_q:
            completed.append(task.name)
            continue

        over = cur_time + task.playtime - wait_q[-1].start

        if over > 0:
            cur_time += task.playtime - over
            task.playtime = over
            ready_q.append(task)
            ready_q.append(wait_q.pop())
        else:
            cur_time += task.playtime
            completed.append(task.name)

            if over == 0:
                ready_q.append(wait_q.pop())

    return completed
