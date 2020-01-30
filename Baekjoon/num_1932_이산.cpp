/*
#2020년 1월 29일
#c++, 우이산
#DP연습
*/

#include <cstdio>

int n = 0;
int** pyramid;
int** dp;

int calculate(const int i, const int j);
int main() {
	scanf("%d", &n);

	pyramid = new int*[n];
	dp = new int* [n];
	
	// get input
	for (int i = 0; i < n; i++) {
		pyramid[i] = new int[i + 1];
		dp[i] = new int[i + 1];
		for (int j = 0; j < i + 1; j++) {
			scanf("%d", &pyramid[i][j]);
			dp[i][j] = -1;
		}
	}

	// print result
	printf("%d\n", calculate(0, 0));

	return 0;
}

int calculate(const int i, const int j) {
	// i is the layers of pyramids
	// j is the index of the layers
	
	// if is out of the pyramid
	if (i == n)
		return 0;

	if (dp[i][j] == -1) {
		int temp1 = calculate(i + 1, j);
		int temp2 = calculate(i + 1, j + 1);

		dp[i][j] = pyramid[i][j] + ((temp1 > temp2) ? temp1 : temp2);
	}

	return dp[i][j];
}