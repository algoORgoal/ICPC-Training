/*
#2020년 1월 17일
#우이산, c++
#11053번 문제
#메모이제이션 버전
*/

#include <cstdio>
#include <vector>

using namespace std;

int calculate(const int & index);

int N;
int* resultArr;
vector<int> v;

int main() {
	scanf("%d", &N);
	resultArr = new int[N];

	for (int i = 0; i < N; i++) {
		int temp;
		scanf("%d", &temp);
		v.push_back(temp);
		resultArr[i] = -1;
	}

	int result = 0;
	for (int i = 0; i < N; i++) {
		int temp = calculate(i);
		result = (result > temp) ? result : temp;
	}

	delete[] resultArr;

	printf("%d\n", result);

	return 0;
}

int calculate(const int & index) {
	if(resultArr[index] != -1)
		return resultArr[index];

	int result = 0;
	for (int i = index; i < N; i++) {
		if (v.at(i) > v.at(index)) {
			int temp = calculate(i);
			result = (result > temp) ? result : temp;
		}
	}

	return (resultArr[index] = result + 1);
};