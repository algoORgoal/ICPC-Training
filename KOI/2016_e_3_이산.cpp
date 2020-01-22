/*
#2020년 1월 22일
#우이산, c++
*/

#include <cstdio>

const int ONE_DAY = 10000;
const int THREE_DAY = 25000;
const int FIVE_DAY = 37000;
const int MAX = 20000000;

int N;
bool* isDaysMustGo;

int** dp;

int calculate(const int& day, int coupon);

int main() {
	scanf("%d", &N);
	isDaysMustGo = new bool[N];
	for (int i = 0; i < N; i++)
		isDaysMustGo[i] = true;
	
	int M;
	scanf("%d", &M);
	for (int i = 0; i < M; i++) {
		int temp;
		scanf("%d", &temp);
		isDaysMustGo[temp - 1] = false;
	}

	// dp[the num of coupon][the day]
	// max coupon num is under 40
	dp = new int*[40];
	for (int coupon = 0; coupon < 40; coupon++) {
		dp[coupon] = new int [N];
		for (int n = 0; n < N; n++) {
			dp[coupon][n] = -1;
		}
	}

	printf("%d\n", calculate(0 /*== starting day*/, 0 /*== the num of coupon*/));

	return 0;
}

int calculate(const int& day, int coupon){
	// if calculate is end in this case
	if (day >= N) {
		return 0;
	}

	if (dp[coupon][day] != -1)
		return dp[coupon][day];

	int result = MAX;
	
	// buy 5-day stroke
	int temp = calculate(day + 5, coupon + 2) + FIVE_DAY;
	result = (result < temp) ? result : temp;

	// buy 3-day stroke
	temp = calculate(day + 3, coupon + 1) + THREE_DAY;
	result = (result < temp) ? result : temp;

	// buy 1-day stroke
	temp = calculate(day + 1, coupon) + ONE_DAY;
	result = (result < temp) ? result : temp;

	// don't buy
	// using coupon
	if (isDaysMustGo[day]) {
		if (coupon >= 3)
			temp = calculate(day + 1, coupon - 3);
		else
			temp = MAX;
	}
	else
		temp = calculate(day + 1, coupon);
	result = (result < temp) ? result : temp;

	dp[coupon][day] = result;

	return dp[coupon][day];
};