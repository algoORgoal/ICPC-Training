#include <cstdio>
#include <set>
#include <vector>

using namespace std;

int main() {
	int N,
		M;

	scanf("%d %d", &N, &M);

	set<int>* setArr = new set<int>[N];
	for (int i = 0; i < M; i++) {
		int x, y;
		scanf("%d %d", &x, &y);

		setArr[x - 1].insert(y);
	}

	vector<int> tempV;
	for (int i = 0; i < N; i++) {
		tempV.push_back(i + 1);
	}
	vector<int> result;
	for (int i = 0; i < N; i++) {
		result.push_back(tempV.at(setArr[i].size()));
		tempV.erase(tempV.begin() += setArr[i].size());
	}

	for (int i = 0; i < N; i++) {
		for (set<int>::iterator it = setArr[i].begin(); it != setArr[i].end(); it++) {
			if (result.at((*it) - 1) > result.at(i)) {
				printf("-1\n");
				return 0;
			}
		}
	}

	for (int i = 0; i < N; i++)
		printf("%d ", result.at(i));
	printf("\n");

	return 0;
}