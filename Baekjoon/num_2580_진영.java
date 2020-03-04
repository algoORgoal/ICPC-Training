package noj.am;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Point { // map의 값이 0인 위치를 저장
	int x;
	int y;

	Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public class Main {
	static int[][] map; // 스도쿠 배열
	static ArrayList<Point> points;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;

		map = new int[10][10];
		points = new ArrayList<>();

		for (int i = 1; i <= 9; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= 9; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j] == 0) {
					points.add(new Point(i, j));
				}
			}
		}

		DFS(0);
		bw.flush();
		bw.close();
		br.close();
	}

	public static void DFS(int index) { // points의 index를 기준으로 탐색.
		if (index == points.size()) { // 탐색을 완료하였으면, 여태까지 저장한 map을 출력함.
			for (int i = 1; i <= 9; i++) {
				for (int j = 1; j <= 9; j++) {
					System.out.print(map[i][j] + " ");
				}
				System.out.println();
			}
			System.exit(0); // 한 번만 출력하고 바로 종료.
		} else {
			Point p = points.get(index);
			for (int i = 1; i <= 9; i++) {
				if (checkMap(p.x, p.y, i)) { // 가로, 세로, 3x3 사각형에서 중복되는 수가 없으면,
					map[p.x][p.y] = i; // 0이었던 위치에 i를 넣어줌.(i는 1~9까지의 수).
					DFS(index + 1); // 다음 인덱스 탐색.
					map[p.x][p.y] = 0; // 백트래킹 -> 만약 그 다음 과정에서 중복되는 경우가 있으면, 바꿔준 값을 다시 0으로 메꿔놓음.
				}
			}
		}
	}

	public static boolean checkMap(int x, int y, int value) { // 가로, 세로, 3x3 사각형을 탐색.
		// 가로
		for (int i = 1; i <= 9; i++) {
			if (map[x][i] == value) { 
				return false;
			}
		}

		// 세로
		for (int i = 1; i <= 9; i++) {
			if (map[i][y] == value) {
				return false;
			}
		}

		// 3x3 사각형
		for(int i = ((x - 1) / 3) * 3 + 1; i < ((x - 1) / 3) * 3 + 4; i++) {
			for(int j = ((y - 1) / 3) * 3 + 1; j < ((y - 1) / 3) * 3 + 4; j++) {
				if(map[i][j] == value) {
					return false;
				}
			}
		}

		return true;
	}

}
