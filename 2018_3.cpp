/*
#2019/12/31 우이산
#2018년 초등부 3번 문제 (메모리 초과)
#작성언어 c++
*/

#include <cstdio>

short*& searchMinPath(short**& arr, const int& N, const int & pivot/*== starting point*/);

int main() {
	int N,
		A, /* == robot A's position*/
		B; /* == robot B's position*/

	scanf("%d %d %d", &N, &A, &B);
	// the index started on 0
	A -= 1;
	B -= 1;

	// make an arr for path's info
	short** pathInfo = new short* [N];
	for (int i = 0; i < N; i++) {
		pathInfo[i] = new short[N];
		for (int j = 0; j < N; j++)
			pathInfo[i][j] = -1;
	}

	// get path info
	for (int i = 0; i < N - 1; i++) {
		int a, /* == a room linked by the path*/
			b, /* == a room linked by the path*/
			weight /* == length of the path */;

		scanf("%d %d %d", &a, &b, &weight);
		pathInfo[a-1][b-1] = pathInfo[b-1][a-1] = weight;
	}

	// get min path
	short * arrA = searchMinPath(pathInfo, N, A);
	short * arrB = searchMinPath(pathInfo, N, B);

	// calculate result
	unsigned long long result = arrA[0] + arrB[0];
	for (int i = 0; i < N; i++) {
		for (int j = i; j < N; j++) {
			if(pathInfo[i][j] != -1)
				result = (result < (arrA[i] + arrB[j]))? result : (arrA[i] + arrB[j]);
		}
	}

	printf("%llu\n", result);

	return 0;
}

short*& searchMinPath(short**& arr, const int& N, const int& pivot/*== starting point*/) {
	// init result array
	short* result = new short[N];
	for (int i = 0; i < N; i++) {
		result[i] = -1;
	}
	result[pivot] = 0;

	int count = 1;
	while (count < N) {
		for (int i = 0; i < N; i++) {
			if (result[i] == -1)
				continue;

			for (int j = 0; j < N; j++) {
				if (result[j] != -1)
					continue;

				if (arr[i][j] != -1) {
					result[j] = result[i] + arr[i][j];
					count++;
				}
			}
		}
	}

	return result;
};