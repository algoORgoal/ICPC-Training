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

		if (N == 1 || M == 1) {
			bw.write("1\n");
			bw.flush();
			bw.close();
			br.close();
			return;
		}

		if (N == 2) {
			if (M <= 2) {
				bw.write("1\n");
				bw.flush();
				bw.close();
				br.close();
				return;
			}

			if (M <= 4) {
				bw.write("2\n");
				bw.flush();
				bw.close();
				br.close();
				return;
			}

			if (M <= 6) {
				bw.write("3\n");
				bw.flush();
				bw.close();
				br.close();
				return;
			}

			bw.write("4\n");
			bw.flush();
			bw.close();
			br.close();
			return;
		}

		if (N >= 3) {
			if (M <= 4) {
				bw.write(M + "\n");
				bw.flush();
				bw.close();
				br.close();
				return;
			}

			if (M <= 6) {
				bw.write("4\n");
				bw.flush();
				bw.close();
				br.close();
				return;
			} else {
				bw.write(4 + (M - 6) + "\n");
				bw.flush();
				bw.close();
				br.close();
				return;
			}
		}

		bw.flush();
		bw.close();
		br.close();
	}

}
