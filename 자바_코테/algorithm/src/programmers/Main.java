package programmers;

import java.util.*;

public class Main {
    static boolean solution(String s) {
        boolean answer = true;

        List<Integer> list = new ArrayList<>();

        Collections.sort(list, Collections.reverseOrder());
        Collections.reverse(list);
        Collections.frequency(list, 23);

        Stack<Integer> stacks = new Stack<>();
        Queue<Integer> q = new LinkedList<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        PriorityQueue<Integer> pq_reverse = new PriorityQueue<>(Collections.reverseOrder());

        pq.clear();

        HashSet<Integer> set = new HashSet<>();
        set.add(1);
        set.add(1);
        set.remove(1);
        set.add(2);
        set.clear();
        set.size();
        set.contains(2);

        for (int d : set) {

        }

        HashMap<String, Integer> map = new HashMap<>();
        map.put("first", 1);
        map.put("second", 2);
        map.put("third", 3);

        map.remove("first");
//        map.clear();

        map.containsKey("first");
        map.containsValue(3);

        for (String j : map.keySet()) {
            System.out.println(map.get(j));
        }


        for (Map.Entry<String, Integer> y : map.entrySet()) {
            System.out.println(y.getKey() + y.getValue());
        }
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push('(');
            }
            else{
                if (!stack.isEmpty()) {
                    if (stack.peek() == '(') {
                        stack.pop();
                    }
                    else{
                        return false;
                    }
                }
                else{
                    return false;
                }
            }
        }
        if (!stack.isEmpty()) {
            answer = false;
        }
        return answer;
    }

    public static void main(String[] args) {
        Map<String, Integer> map = new LinkedHashMap<>();

        map.put("apple", 1);

        for (String key : map.keySet()) {
            System.out.println(map.get(key));
        }
        
    }

}
