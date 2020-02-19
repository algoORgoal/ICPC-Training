package noj.am;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Point {
	int x, y;

	Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public class Main {
	static int[] rangeX = { -1, 0, 1, 0 };
	static int[] rangeY = { 0, 1, 0, -1 };
	static int N;
	static int[][] map;
	static boolean[][] visit;
	static int cnt;
	static int result;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		N = Integer.parseInt(br.readLine());
		map = new int[N + 1][N + 1];
		visit = new boolean[N + 1][N + 1];
		StringTokenizer st;

		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (!visit[i][j] && map[i][j] == 1) {
					DFS(i, j);
					cnt++;
				}
			}
		}

		int ans = Integer.MAX_VALUE;
		for (int i = 2; i <= cnt; i++) {
			BFS(i);
			ans = Math.min(result, ans);
		}

		bw.write(ans + "\n");
		bw.close();
		br.close();
	}

	public static void DFS(int x, int y) {
		visit[x][y] = true;
		map[x][y] += cnt + 1;
		int dx, dy;

		for (int i = 0; i < 4; i++) {
			dx = x + rangeX[i];
			dy = y + rangeY[i];

			if (dx < 1 || dy < 1 || dx > N || dy > N) {
				continue;
			}

			if (!visit[dx][dy] && map[dx][dy] == 1) {
				DFS(dx, dy);
			}
		}

	}

	public static void BFS(int start) {
		Queue<Point> q = new LinkedList<>();
		int x, y;
		boolean[][] sea = new boolean[N + 1][N + 1];
		result = 0;

		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (map[i][j] == start) {
					q.add(new Point(i, j));
				}
			}
		}

		while (!q.isEmpty()) {
			int qSize = q.size();
			for (int j = 0; j < qSize; j++) {
				Point point = q.poll();
				for (int i = 0; i < 4; i++) {
					x = point.x + rangeX[i];
					y = point.y + rangeY[i];

					if (x < 1 || y < 1 || x > N || y > N) {
						continue;
					}

					if (map[x][y] == 0 && !sea[x][y]) {
						sea[x][y] = true;
						map[x][y] = start;
						q.add(new Point(x, y));
					} else if (map[x][y] == start) {
						continue;
					} else {
						for (int k = 1; k <= N; k++) {
							for (int m = 1; m <= N; m++) {
								if (sea[k][m]) {
									map[k][m] = 0;
								}
							}
						}
						return;
					}

				}
			}
			result++;
		}
	}

}
