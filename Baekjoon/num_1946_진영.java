package noj.am;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;

		int T = Integer.parseInt(br.readLine());

		for (int i = 0; i < T; i++) {
			int N = Integer.parseInt(br.readLine());
			int[] employees = new int[N + 1]; // employees[1] = 4�̶��, ���� ���� 1���� �������� ���� ������ 4����.
			for (int j = 0; j < N; j++) { // �Է�
				st = new StringTokenizer(br.readLine());
				int t = Integer.parseInt(st.nextToken());
				int f = Integer.parseInt(st.nextToken());

				employees[t] = f;
			}

			int maxInterview = employees[1]; // employees[1]�� ���� ������ 1���̹Ƿ� ������ �հ��ڿ� �����ؾ� ��.
			int ans = 1;
			for(int k = 2; k <= N; k++) {
				if(employees[k] < maxInterview) { // maxInterview���� ������ ���� �����ڰ� ��Ÿ����,
					maxInterview = employees[k]; // �� �������� ���� ������ �ʱ�ȭ�� ��.
					ans++;
				}
			}
			bw.write(ans + "\n");
		}

		bw.flush();
		bw.close();
		br.close();
	}

}
