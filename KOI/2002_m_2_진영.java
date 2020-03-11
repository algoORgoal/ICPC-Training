package noj.am;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Coin {
	int price;
	int cnt;

	Coin(int price, int cnt) {
		this.price = price;
		this.cnt = cnt;
	}
}

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;

		int T = Integer.parseInt(br.readLine());
		int K = Integer.parseInt(br.readLine());

		Coin[] coins = new Coin[K + 1];

		for (int i = 1; i <= K; i++) {
			st = new StringTokenizer(br.readLine());
			int price = Integer.parseInt(st.nextToken());
			int cnt = Integer.parseInt(st.nextToken());

			coins[i] = new Coin(price, cnt);
		}

		int[][] dp = new int[K + 1][T + 1];
		dp[0][0] = 1;
		
		// ���� ������ �����ذ��� ����.
		for (int i = 1; i <= K; i++) { // ������ ����
			for (int k = 0; k <= coins[i].cnt; k++) { // 0�� ~ �� ������ �ִ� ����
				for (int j = 0; j <= T; j++) { // ������ �ݾ�
					if (j + coins[i].price * k > T) {
						break;
					}
					dp[i][j + coins[i].price * k] += dp[i - 1][j];
				}
			}
		}

		bw.write(dp[K][T] + "\n");
		bw.flush();
		bw.close();
		br.close();
	}

}
