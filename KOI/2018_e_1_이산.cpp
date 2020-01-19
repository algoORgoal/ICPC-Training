/*
#2018년 한국 정보 올림피아드 초등부 문제 1번
#2019년 12월 24일 해결
#우이산
#
#추가논의사항 없음
*/

#include <cstdio>

int main() {

	int numOfStd = 0;
	scanf("%d", &numOfStd);

	int* stdArr = new int[numOfStd];
	for (int i = 0; i < numOfStd; i++) {
		scanf("%d", &stdArr[i]);
	}

	int max, min;
	max = min = stdArr[0];
	for (int i = 1; i < numOfStd; i++) {
		if (max < stdArr[i])
			max = stdArr[i];

		if (min > stdArr[i])
			min = stdArr[i];
	}

	printf("%d", max - min);

	return 0;
}