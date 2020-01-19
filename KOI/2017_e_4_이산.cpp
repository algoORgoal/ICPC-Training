/*
#2017년 초등부 4번 문제
#우이산
#작성언어 c++
*/

#include<cstdio>
#include<set>

using namespace std;

int main() {
	int N,
		M;

	scanf("%d %d", &N, &M);

	set<int>* setArr = new set<int>[N];
	for (int i = 0; i < M; i++) {
		int x, y;
		scanf("%d %d", &x, &y);

		// x학생의 카드보다 y학생의 카드가 작다
		// (x는 y앞에 있다)
		setArr[x - 1].insert(y);
	}

	// n번째 학생이 가진 카드 번호들의 배열
	int* resultArr = new int[N];
	
	// 아래는 카드 번호를 결정하는 과정
	// pjy1368의 아이디어가 훨씬 직관적이고 효과적인것으로 보인다
	// 근본은 같은 아이디어지만 훨씬 복잡하고 난해하기 때문에
	// 아래 코드에 대한 설명은 하지 않도록 하겠다
	for (int i = 0; i < N; i++)
		resultArr[i] = i + 1;
	for (int i = 0; i < N; i++) {
		resultArr[i] += setArr[i].size();

		for(set<int>::iterator it = setArr[i].begin() ; it != setArr[i].end(); it++){
			resultArr[(*it) - 1] --;
		}
	}

	// 만약 같은 카드 번호를 가진
	// 즉, 유효하지 않은 입력인 경우를
	// 가려내기 위한 코드
	bool* errorCheckArr = new bool[N];
	for (int i = 0; i < N; i++) {
		errorCheckArr[i] = false;
	}
	for (int i = 0; i < N; i++) {
		if (errorCheckArr[resultArr[i] - 1]) {
			printf("-1\n");
			return 0;
		}
		else {
			errorCheckArr[resultArr[i] - 1] = true;
		}
	}

	for (int i = 0; i < N; i++)
		printf("%d ", resultArr[i]);
	printf("\n");

	return 0;
}