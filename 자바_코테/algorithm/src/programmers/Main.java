package programmers;

import java.util.*;

public class Main {
    public static int[] solution(String[] genres, int[] plays) { //int[]
        ArrayList<Integer> answer = new ArrayList<>();
        HashMap<String, Integer> total = new HashMap<>();
        HashMap<String, HashMap<Integer, Integer>> music = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            if (!total.containsKey(genres[i])) {
                HashMap<Integer, Integer> map = new HashMap<>();
                map.put(i, plays[i]);
                music.put(genres[i], map); //그리고 아이디랑, 재색수 저장
                total.put(genres[i], plays[i]); //없으면 초기 값으로 plays[i] 값
            } else {
                music.get(genres[i]).put(i, plays[i]);
                total.put(genres[i], plays[i] + total.get(genres[i]));
            }
        }

        List<String> total_keySet = new ArrayList<>(total.keySet());
        Collections.sort(total_keySet, (s1, s2) -> total.get(s2) - (total.get(s1))); //내림차순

        for (String key : total_keySet) {
            HashMap<Integer, Integer> map = music.get(key);
            List<Integer> music_keySet = new ArrayList<>(map.keySet());
            Collections.sort(music_keySet, (s1, s2) -> map.get(s2) - (map.get(s1)));

            answer.add(music_keySet.get(0));
            if (music_keySet.size() > 1) {
                answer.add(music_keySet.get(1));
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
    public static void main(String[] args){
        String[] genres = {"classic", "pop", "classic", "classic", "pop"};
        int[] plays = {500, 600, 150, 800, 2500};
        int[] solution = solution(genres, plays);
        for (int v : solution) {
            System.out.print(v+" ");
        }
    }
}
