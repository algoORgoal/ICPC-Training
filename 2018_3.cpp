/*
#2019/12/31 우이산
#2018년 초등부 3번 문제 (메모리 초과)
#작성언어 c++
*/

#include <cstdio>
#include <vector>

using namespace std;

typedef struct path {
	int dest;
	int weight;
}Path;

typedef struct node {
	vector<Path> v;
}Node;

// return an int array that store distance to others
int*& searchMinPath(Node *& arr, const int& N, const int & pivot/*== starting point*/);

// Return distance between n1 and n2
int howFar(Node &n1, const int& n2);

int main() {
	int N,
		A, /* == robot A's position*/
		B; /* == robot B's position*/

	scanf("%d %d %d", &N, &A, &B);
	// the index started on 0
	A -= 1;
	B -= 1;

	// make an arr for node's info
	Node* nodeInfo = new Node[N];

	// get path info
	for (int i = 0; i < N - 1; i++) {
		int a, /* == a room linked by the path*/
			b, /* == a room linked by the path*/
			weight /* == length of the path */;

		scanf("%d %d %d", &a, &b, &weight);
		// the index started on 0
		nodeInfo[a - 1].v.push_back({ b - 1, weight });
		nodeInfo[b - 1].v.push_back({ a - 1, weight });
	}

	// get min path
	int * arrA = searchMinPath(nodeInfo, N, A);
	int * arrB = searchMinPath(nodeInfo, N, B);

	// calculate result
	int result = arrA[0] + arrB[0];
	for (int i = 0; i < N; i++) {
		for (int j = i; j < N; j++) {
			// if there is a path link i to j
			if (howFar(nodeInfo[i], j) != -1)
				result = (result < (arrA[i] + arrB[j]))? result : (arrA[i] + arrB[j]);
		}
	}

	printf("%d\n", result);

	return 0;
}

int howFar(Node & n1, const int& n2) {
	for (int i = 0; i < n1.v.size(); i++) {
		if (n1.v.at(i).dest == n2)
			return n1.v.at(i).weight;
	}
	return -1;
};

int*& searchMinPath(Node*& arr, const int& N, const int& pivot/*== starting point*/) {
	// init result array
	int* result = new int[N];
	for (int i = 0; i < N; i++) {
		result[i] = -1;
	}
	result[pivot] = 0;

	int count = 1;
	while (count < N) {
		for (int i = 0; i < N; i++) {
			// i까지의 경로를 찾지 못했다면
			if (result[i] == -1)
				continue;

			for (int j = 0; j < N; j++) {
				// j까지의 경로를 이미 알고 있다면
				if (result[j] != -1)
					continue;

				// i와 j사이를 연결하는 통로가 있다면
				int distance = howFar(arr[i], j);
				if (distance != -1) {
					result[j] = result[i] + distance;
					count++;
				}
			}
		}
	}

	return result;
};