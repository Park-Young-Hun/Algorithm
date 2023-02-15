package Programmers;

import java.util.*;

public class Disguise {
    public int solution(String[][] clothes) {
        int answer = 1;

        HashMap<String, List<String>> clothMap = new HashMap<>();

        for (int i=0; i<clothes.length; i++) {
            List<String> clothNames = new ArrayList<>();
            clothMap.put(clothes[i][1], clothNames);
        }

        for (int i=0; i<clothes.length; i++) {
            clothMap.get(clothes[i][1]).add(clothes[i][0]);
        }

        for (String key : clothMap.keySet()) {
            List<String> clothNames = clothMap.get(key);
            answer *= clothNames.size() + 1; // 안고르는 경우가 있기 때문에 +1해서 서로 곱한다.
        }
        return answer-1; // 아무옷도 안입는 경우는 제외한다.
    }
}
