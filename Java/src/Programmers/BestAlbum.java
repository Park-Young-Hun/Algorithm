package Programmers;

import java.util.*;

public class BestAlbum {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};

        HashMap<String, List<List<Integer>>> genreMap = new HashMap<>();

        for (int i=0; i<genres.length; i++) {
            if (!genreMap.containsKey(genres[i])) {
                List<List<Integer>> songs = new ArrayList<>();
                genreMap.put(genres[i], songs);
            }
        }

        for (int i=0; i<genres.length; i++) {
            List<Integer> song = new ArrayList<>();
            song.add(i);
            song.add(plays[i]);
            genreMap.get(genres[i]).add(song);
        }
        System.out.println(genreMap);
        return answer;
    }
}
