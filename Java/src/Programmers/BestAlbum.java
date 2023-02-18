package Programmers;

import java.util.*;

public class BestAlbum {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();

        HashMap<String, List<List<Integer>>> genreMap = new HashMap<>();
        HashMap<Integer, String> playMap = new HashMap<>();
        List<Integer> playSums = new ArrayList<>();

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

        for (String key : genreMap.keySet()) {
            Integer playSum = 0;

            genreMap.get(key).sort(
                    (s1, s2) -> s1.get(1).equals(s2.get(1)) ? s1.get(0) - s2.get(0) : s2.get(1) - s1.get(1)
            );

            for (List<Integer> songs : genreMap.get(key)) {
                playSum += songs.get(1);
            }
            playMap.put(playSum, key);
            playSums.add(playSum);
        }
        playSums.sort(Collections.reverseOrder());

        for (Integer playSum : playSums) {
            String genre = playMap.get(playSum);
            List<List<Integer>> songs = genreMap.get(genre);

            answer.add(songs.get(0).get(0));

            if (songs.size() > 1) {
                answer.add(songs.get(1).get(0));
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
