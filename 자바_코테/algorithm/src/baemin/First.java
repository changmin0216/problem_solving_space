package baemin;
import java.util.*;

public class First {
    static class Edge implements Comparable<Edge>{
        int dest;
        int weight;
        public Edge(int dest, int weight){
            this.dest = dest;
            this.weight = weight;
        }
        @Override
        public int compareTo(Edge o){
            return weight - o.weight;
        }
    }
    static ArrayList<Edge>[] graph;
    public static int dijkstra(int n, int start, int k){
        boolean[] visited = new boolean[n + 1];
        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);

        dist[start] = 0;
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        pq.add(new Edge(start, 0));

        while(!pq.isEmpty()){
            Edge curr = pq.poll();

            for (Edge edge : graph[curr.dest]) {
                if (dist[edge.dest] > dist[curr.dest] + edge.weight) {
                    dist[edge.dest] = dist[curr.dest] + edge.weight;

                    pq.add(new Edge(edge.dest, dist[edge.dest]));
                }
            }
        }
        int cnt=0;
        for (int i : dist) {
            if (cnt <= k){
                cnt++;
            }
        }
        return cnt;
    }

    public static int solution(int N, int[][] road, int K) {
        int answer=0;

        graph = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i=0;i<road.length;i++){
            int a = road[i][0];
            int b = road[i][1];
            int weight = road[i][2];

            graph[a].add(new Edge(b, weight));
            graph[b].add(new Edge(a, weight));
        }

        answer = dijkstra(N, 1, K);

        return answer;
    }

    public static void main(String[] args){
        int[][] road = {{1,2,1}, {2,3,3}, {5,2,2}, {1,4,2}, {5,3,1},{5,4,2}};
        System.out.println(solution(5, road, 3));
    }
}

