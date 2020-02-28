// If you change the constant 20000 to a variable (of course, the value is the same), you get 'wrong' from baekjoon.

#include <cstdio>

int main() {
	int n, k;
	scanf("%d %d", &n, &k);

	int* coin = new int[n];
	for (int i = 0; i < n; i++) {
		int temp;
		scanf("%d", &temp);

		for (int j = 0; j < i; j++) {
			if (coin[j] == temp) {
				temp = 20000;
				break;
			}
		}

		coin[i] = temp;
	}

	int* dp = new int[k + 1];
	for (int i = 0; i < k + 1; i++) {
		dp[i] = 20000;
	}
	dp[0] = 0;

	for (int coinNum = 0; coinNum < n; coinNum++) {
		for (int price = coin[coinNum]; price < k + 1; price++) {
			int older = dp[price];
			int newer = dp[price - coin[coinNum]] + 1;
			dp[price] = (older < newer) ? older : newer;
		}
	}

	if (dp[k] != 0 && dp[k] != 20000)
		printf("%d\n", dp[k]);
	else
		printf("-1\n");

	delete[] coin;
	delete[] dp;
	return 0;
}