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
			int[] employees = new int[N + 1]; // employees[1] = 4이라면, 서류 순위 1등인 지원자의 면접 순위는 4등임.
			for (int j = 0; j < N; j++) { // 입력
				st = new StringTokenizer(br.readLine());
				int t = Integer.parseInt(st.nextToken());
				int f = Integer.parseInt(st.nextToken());

				employees[t] = f;
			}

			int maxInterview = employees[1]; // employees[1]는 서류 순위가 1등이므로 무조건 합격자에 포함해야 함.
			int ans = 1;
			for(int k = 2; k <= N; k++) {
				if(employees[k] < maxInterview) { // maxInterview보다 순위가 높은 지원자가 나타나면,
					maxInterview = employees[k]; // 그 지원자의 면접 순위로 초기화를 함.
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
