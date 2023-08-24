import java.util.*;

class Process {
    int priority;
    int location;

    public Process(int priority, int location) {
        this.priority = priority;
        this.location = location;
    }
}

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;

        Deque<Process> queue = new ArrayDeque<>();

        for (int i=0; i<priorities.length; i++) {
            Process process = new Process(priorities[i], i);
            queue.add(process);
        }

        while (!queue.isEmpty()) {
            boolean isFirst = true;
            Process cur = queue.remove();

            for (Process process : queue) {
                if (cur.priority < process.priority) {
                    queue.add(cur);
                    isFirst = false;
                    break;
                }
            }

            if (isFirst) {
                if (cur.location == location) {
                    return answer;
                }
                else {
                    answer++;
                }
            }
        }
        return answer;
    }
}
