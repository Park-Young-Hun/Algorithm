package Programmers;

import java.util.*;

class MoreSpicy {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (int num : scoville) {
            minHeap.add(num);
        }

        while (minHeap.peek() < K) {
            if (minHeap.size() < 2) {
                return -1;
            }
            int first = minHeap.poll();
            int second = minHeap.poll();
            minHeap.add(first + 2*second);
            answer++;
        }
        return answer;
    }
}
