/*
#2020년 1월 21일
#우이산, c++
#직관성이 떨어지는 코드
*/

#include <cstdio>

int n;
int* result;

int main() {
	scanf("%d", &n);

	// n이 홀수라면 경우의 수가 존재하지 않음
	if (n % 2 == 1) {
		printf("0\n");
		return 0;
	}

	n /= 2;
	result = new int[n+1];

	// result[0]은 n이 0인 경우
	// 즉, 아무 블럭도 없는 경우를 의미
	result[0] = 1;
	for (int i = 1; i < n+1; i++) {
		// 마지막이 누운 블럭 3개인 경우
		// 즉, i-2번째 줄까지 다 채워졌고 (result[i-1])
		// 그 이후에 누운블럭 3개를 채운 경우
		result[i] = result[i-1]*3;

		for (int j = 0; j < i-1; j++) {
			// 마지막이 누운블럭 1개와 세운블럭 1개인 경우
			// j번째 줄까지 다 채워졌고 (result[j*2])
			// 그 이후에 i번째 줄까지 '완전히'채워진 경우가 없는 상황
			// 끝에 아래블럭이 누운경우와 윗블럭이 누운경우 2가지로 나뉨
			result[i] += result[j] * 2;
		}
	}

	printf("%d\n", result[n]);
	return 0;
}