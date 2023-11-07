package Programmers;

import java.util.*;


class HIndex {
    public int solution(int[] citations) {
        int answer = 0;
        int n = citations.length;
        Arrays.sort(citations);

        for (int i = 0; i < n; i++) {
            if (citations[i] >= n-i) {
                answer = n-i;
                break;
            }
        }

        return answer;
    }
}

