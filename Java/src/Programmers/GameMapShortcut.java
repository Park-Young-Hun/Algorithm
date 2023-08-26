import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int depth = 1;
        int n = maps.length;
        int m = maps[0].length;

        int[] delta_row = {1, -1, 0 ,0};
        int[] delta_col = {0, 0, 1, -1};

        Deque<List<Integer>> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];

        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                visited[i][j] = false;
            }
        }

        List<Integer> start = new ArrayList<>(List.of(0, 0));
        queue.add(start);
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            int len = queue.size();
            for (int i=0; i<len; i++) {
                List<Integer> cur = queue.remove();

                if (cur.get(0) == n-1 && cur.get(1) == m-1) {
                    return depth;
                }

                for (int j=0; j<4; j++) {
                    int new_row = cur.get(0) + delta_row[j];
                    int new_col = cur.get(1) + delta_col[j];

                    if (new_row < 0 || new_row >= n || new_col < 0 || new_col >= m) {
                        continue;
                    }

                    if (!visited[new_row][new_col] && maps[new_row][new_col] == 1) {
                        List<Integer> next = new ArrayList<>(List.of(new_row, new_col));
                        visited[new_row][new_col] = true;
                        queue.add(next);
                    }
                }
            }
            depth++;
        }
        return -1;
    }
}