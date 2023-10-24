package Programmers;

import java.util.*;

class Task {
    private int requestTime; // 요청시간
    private int turnaroundTime; // 소요시간

    public Task(int requestTime, int turnaroundTime) {
        this.requestTime = requestTime;
        this.turnaroundTime = turnaroundTime;
    }

    public int getRequestTime() {
        return requestTime;
    }

    public int getTurnaroundTime() {
        return turnaroundTime;
    }
}


public class DiskController {
    public int solution(int[][] jobs) {
        int curTime = 0; // 현재시각
        List<Integer> result = new ArrayList<>();
        List<Task> tasks = new ArrayList<>();

        for (int i = 0; i < jobs.length; i++) {
            tasks.add(new Task(jobs[i][0], jobs[i][1]));
        }

        // 요청시간이 이른순, 소요시간 짧은순으로 정렬.
        tasks.sort(
                (task1, task2) -> {
                    int compareByRequestTime = Integer.compare(task1.getRequestTime(), task2.getRequestTime());

                    if (compareByRequestTime != 0) {
                        return compareByRequestTime;
                    }
                    else {
                        return Integer.compare(task1.getTurnaroundTime(), task2.getTurnaroundTime());
                    }
                }
        );

        Deque<Task> waitQ = new ArrayDeque<>(tasks);

        // 하나의 작업이 실행되는 동안 이미 들어온 작업들은 소요시간 짧은 것 부터 우선적으로 처리.
        PriorityQueue<Task> readyQ = new PriorityQueue<>(
                (task1, task2) -> {
                    int compareByTurnaroundTime = Integer.compare(task1.getTurnaroundTime(), task2.getTurnaroundTime());

                    if (compareByTurnaroundTime != 0) {
                        return compareByTurnaroundTime;
                    }
                    else {
                        return Integer.compare(task1.getRequestTime(), task2.getRequestTime());
                    }
                }
        );

        while (!waitQ.isEmpty() || !readyQ.isEmpty()) {

            // 처리할 요청이 없으면 waitQ에서 하나 가져와서 처리.
            if (readyQ.isEmpty()) {
                curTime = waitQ.element().getRequestTime();
                readyQ.add(waitQ.remove());
            }

            Task task = readyQ.remove();
            result.add(curTime - task.getRequestTime() + task.getTurnaroundTime());
            curTime += task.getTurnaroundTime();

            // 하나의 작업을 처리하는 동안 들어온 요청들을 우선순위 큐에 넣어줌.
            while (!waitQ.isEmpty() && waitQ.element().getRequestTime() <= curTime) {
                readyQ.add(waitQ.remove());
            }
        }

        return (int)result.stream().mapToInt(Integer::intValue).average().orElse(0.0);
    }
}
