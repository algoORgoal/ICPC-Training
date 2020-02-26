package noj.am;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Point {
	int location;
	int time;

	Point(int location, int time) {
		this.location = location;
		this.time = time;
	}
}

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken()); // 수빈의 위치
		int K = Integer.parseInt(st.nextToken()); // 동생의 위치

		if (N > K) {
			bw.write((N - K) + "\n");
			bw.flush();
			bw.close();
			br.close();
			return;
		} else if (N == K) {
			bw.write("0\n");
			bw.flush();
			bw.close();
			br.close();
			return;
		}

		bw.write(BFS(N, K) + "\n");
		bw.flush();
		bw.close();
		br.close();
	}

	public static int BFS(int N, int K) {
		Point point = new Point(N, 0);
		Queue<Point> q = new LinkedList<>();
		q.add(point);

		boolean[] visit = new boolean[100001];
		visit[point.location] = true;

		while (!q.isEmpty()) {
			Point subin = q.poll();

			if (K == subin.location) {
				return subin.time;
			}

			if (subin.location - 1 >= 0 && !visit[subin.location - 1]) {
				q.add(new Point(subin.location - 1, subin.time + 1));
				visit[subin.location - 1] = true;
			}

			if (subin.location + 1 <= 100000 && !visit[subin.location + 1]) {
				q.add(new Point(subin.location + 1, subin.time + 1));
				visit[subin.location + 1] = true;
			}

			if (subin.location * 2 <= 100000 && !visit[subin.location * 2]) {
				q.add(new Point(subin.location * 2, subin.time + 1));
				visit[subin.location * 2] = true;
			}
		}

		return 0;
	}

}
