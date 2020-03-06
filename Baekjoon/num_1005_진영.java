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
	static int[] inDegree; // ��������
	static int[] time; // �� �ǹ����� �������� �ð�
	static ArrayList<ArrayList<Integer>> a; // ���� ����Ʈ
	static int endV; // ������ϴ� ���� �ǹ�
	static StringBuilder sb;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine()); // �ݺ� Ƚ��

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

			for (int i = 0; i < e; i++) { // ���� �׷���
				st = new StringTokenizer(br.readLine());
				int t = Integer.parseInt(st.nextToken());
				int f = Integer.parseInt(st.nextToken());

				a.get(t).add(f);
				inDegree[f]++; // ���� ���� ����
			}

			endV = Integer.parseInt(br.readLine());
			topologicalSort();
		}

		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}

	public static void topologicalSort() { // ���� ����
		int[] result = new int[v + 1];
		Queue<Integer> q = new LinkedList<>();

		// ���� ������ 0�� ��带 ť�� ����.
		for (int i = 1; i <= v; i++) {
			if (inDegree[i] == 0) {
				q.offer(i);
				result[i] = time[i];
			}
		}

		// ����� ������ŭ �ݺ����� ����.
		for (int i = 1; i <= v; i++) {
			// n���� �湮�ϱ� ���� ť�� �������� ����Ŭ�� �߻�.
			if (q.isEmpty()) {
				return;
			}

			int now = q.poll();

			if (now == endV) { // �������� ������ϴ� �ǹ��� �Ǹ�, �� �ð��� ����ϰ� ����.
				sb.append(result[now] + "\n");
				return;
			}

			for (int j = 0; j < a.get(now).size(); j++) {
				int next = a.get(now).get(j);

				// ���Ӱ� ���������� 0�� �� ������ ť�� �߰�.
				if (--inDegree[next] == 0) {
					q.offer(next);
				}

				if (result[next] < result[now] + time[next]) {
					// ���� 5�� 6�� �������� 7�� ���� �� �ִٰ� ��������.
					// �� ��, 5���� ���� �ð��� 38��, 6���� ���� �ð��� 18��,�׸��� 7 �ϳ��� ���� �ð��� 1�ʶ�� �ϸ�,
					// 7�� ���� �� �ɸ��� �ð��� 18 + 1�� �ƴ϶� 38 + 1�� �Ǿ�� ��.
					result[next] = result[now] + time[next];
				}

			}
		}
	}
}
