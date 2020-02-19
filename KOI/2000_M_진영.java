package noj.am;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static int[][] map;
	static int[] rangeX = { -1, 0, 1, 0 };
	static int[] rangeY = { 0, 1, 0, -1 };

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken()); // 세로
		M = Integer.parseInt(st.nextToken()); // 가로

		map = new int[N + 1][M + 1];
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int ans = 0;
		for(ans = 0; !isCheese(); ans++) {
			DFS(1,1);
		}
		
		bw.write(ans + "\n");
		bw.flush();
		bw.close();
		br.close();
	}

	public static void DFS(int x, int y) {
		int dx;
		int dy;
		map[x][y] = -1;

		for (int i = 0; i < 4; i++) {
			dx = x + rangeX[i];
			dy = y + rangeY[i];

			if (dx < 1 || dy < 1 || dx > N || dy > M) {
				continue;
			}

			if (map[dx][dy] == 0) {
				DFS(dx, dy);
			}
			
			if (map[dx][dy] > 0) {
				map[dx][dy]++;
			}
		}
	}
	
	public static boolean isCheese() {
		int cnt = 0;
		for (int i = 1; i < N; i++) {
			for (int j = 1; j < M; j++) {
				if(map[i][j] == 1 || map[i][j] == 2) {
					map[i][j] = 1;
					cnt++;
				} else {
					map[i][j] = 0;
				}
			}
		}
		return cnt == 0;
	}

}
