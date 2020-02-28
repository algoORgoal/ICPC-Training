#include <cstdio>

int main() {
	int n, k;
	scanf("%d %d", &n, &k);

	int* coin = new int[n];
	for (int i = 0; i < n; i++) {
		int temp;
		scanf("%d", &temp);
		coin[i] = temp;
	}

	int* dp = new int[k + 1]; 
	for (int i = 0; i < k + 1; i++) {
		dp[i] = 0;
	}
	dp[0] = 1;

	// The numbers in each case are sorted in ascending order
	for (int coinNum = 0; coinNum < n; coinNum++) {
		for (int price = coin[coinNum]; price < k + 1; price++) {
			dp[price] += dp[price - coin[coinNum]];
		}
	}

	printf("%d\n", dp[k]);

	delete[] coin;
	delete[] dp;
	return 0;
}