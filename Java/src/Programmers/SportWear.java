package Programmers;

import java.util.*;

class SportWear {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;

        Set<Integer> lostSet = new HashSet<>();
        Set<Integer> reserveSet = new HashSet<>();


        for (int student : lost) {
            lostSet.add(student);
        }

        for (int student : reserve) {
            reserveSet.add(student);
        }

        Set<Integer> temp = new HashSet<>(lostSet);

        temp.removeAll(reserveSet);
        reserveSet.removeAll(lostSet);
        lostSet = temp;
        answer += n - lostSet.size();

        List<Integer> lostList = new ArrayList<>(lostSet);

        for (int student : lostList) {
            if (reserveSet.contains(student-1)) {
                reserveSet.remove(student-1);
                answer++;
            }
            else if (reserveSet.contains(student+1)) {
                reserveSet.remove(student+1);
                answer++;
            }
        }
        return answer;
    }
}
