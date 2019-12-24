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