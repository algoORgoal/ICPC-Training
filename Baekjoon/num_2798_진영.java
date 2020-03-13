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
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		int[] arr = new int[N];
		
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int ans = Integer.MIN_VALUE;
		int sum = 0;
		for(int i = 0; i < N; i++) {
			sum += arr[i];
			for(int j = i + 1; j < N; j++) {
				sum += arr[j];
				for(int k = j + 1; k < N; k++) {
					sum += arr[k];
					
					if(sum <= M) {
						ans = Math.max(ans, sum);
					}
					
					sum -= arr[k];
				}
				sum -= arr[j];
			}
			sum -= arr[i];
		}
		
		bw.write(ans + "\n");
		bw.flush();
		bw.close();
		br.close();
	}

}
