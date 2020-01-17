/*
#2020년 1월 17일
#우이산, c++
#2016년 초등부 2번 문제
*/

#include <cstdio>

int N;
long long* fibonacci;

int main() {
	scanf("%d", &N);

	if (N == 1) {
		printf("4\n");
		return 0;
	}

	fibonacci = new long long[N];

	fibonacci[0] = 1;
	fibonacci[1] = 1;

	for (int i = 2; i < N; i++)
		fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];

	printf("%lld\n", fibonacci[N - 2] * 2 + fibonacci[N - 1] * 4);

	delete[] fibonacci;

	return 0;
}