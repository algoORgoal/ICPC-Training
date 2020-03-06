package noj.am;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int v, e;
	static int[] inDegree; // 진입차수
	static int[] time; // 각 건물마다 지어지는 시간
	static ArrayList<ArrayList<Integer>> a; // 인접 리스트
	static int endV; // 지어야하는 최종 건물
	static StringBuilder sb;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine()); // 반복 횟수

		for (int n = 0; n < T; n++) {
			st = new StringTokenizer(br.readLine());

			v = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());

			inDegree = new int[v + 1];
			a = new ArrayList<>();

			time = new int[v + 1];

			st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= v; i++) {
				time[i] = Integer.parseInt(st.nextToken());
			}

			for (int i = 0; i <= v; i++) {
				a.add(new ArrayList<>());
			}

			for (int i = 0; i < e; i++) { // 방향 그래프
				st = new StringTokenizer(br.readLine());
				int t = Integer.parseInt(st.nextToken());
				int f = Integer.parseInt(st.nextToken());

				a.get(t).add(f);
				inDegree[f]++; // 진입 차수 증가
			}

			endV = Integer.parseInt(br.readLine());
			topologicalSort();
		}

		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}

	public static void topologicalSort() { // 위상 정렬
		int[] result = new int[v + 1];
		Queue<Integer> q = new LinkedList<>();

		// 진입 차수가 0인 노드를 큐에 삽입.
		for (int i = 1; i <= v; i++) {
			if (inDegree[i] == 0) {
				q.offer(i);
				result[i] = time[i];
			}
		}

		// 노드의 개수만큼 반복문을 수행.
		for (int i = 1; i <= v; i++) {
			// n개를 방문하기 전에 큐가 비어버리면 사이클이 발생.
			if (q.isEmpty()) {
				return;
			}

			int now = q.poll();

			if (now == endV) { // 최종으로 지어야하는 건물이 되면, 총 시간을 출력하고 종료.
				sb.append(result[now] + "\n");
				return;
			}

			for (int j = 0; j < a.get(now).size(); j++) {
				int next = a.get(now).get(j);

				// 새롭게 진입차수가 0인 된 정점을 큐에 추가.
				if (--inDegree[next] == 0) {
					q.offer(next);
				}

				if (result[next] < result[now] + time[next]) {
					// 만약 5와 6이 지어져야 7을 지을 수 있다고 가정하자.
					// 이 때, 5까지 짓는 시간이 38초, 6까지 짓는 시간이 18초,그리고 7 하나를 짓는 시간이 1초라고 하면,
					// 7을 짓는 데 걸리는 시간은 18 + 1이 아니라 38 + 1이 되어야 함.
					result[next] = result[now] + time[next];
				}

			}
		}
	}
}
