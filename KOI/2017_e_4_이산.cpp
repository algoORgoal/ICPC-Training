/*
#2017�� �ʵ�� 4�� ����
#���̻�
#�ۼ���� c++
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

		// x�л��� ī�庸�� y�л��� ī�尡 �۴�
		// (x�� y�տ� �ִ�)
		setArr[x - 1].insert(y);
	}

	// n��° �л��� ���� ī�� ��ȣ���� �迭
	int* resultArr = new int[N];
	
	// �Ʒ��� ī�� ��ȣ�� �����ϴ� ����
	// pjy1368�� ���̵� �ξ� �������̰� ȿ�����ΰ����� ���δ�
	// �ٺ��� ���� ���̵������ �ξ� �����ϰ� �����ϱ� ������
	// �Ʒ� �ڵ忡 ���� ������ ���� �ʵ��� �ϰڴ�
	for (int i = 0; i < N; i++)
		resultArr[i] = i + 1;
	for (int i = 0; i < N; i++) {
		resultArr[i] += setArr[i].size();

		for(set<int>::iterator it = setArr[i].begin() ; it != setArr[i].end(); it++){
			resultArr[(*it) - 1] --;
		}
	}

	// ���� ���� ī�� ��ȣ�� ����
	// ��, ��ȿ���� ���� �Է��� ��츦
	// �������� ���� �ڵ�
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