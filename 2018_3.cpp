/*
#2019/1/1 ���̻�
#2018�� �ʵ�� 3�� ����
#�ۼ���� c++
*/

#include <cstdio>
#include <utility>
#include <vector>
#include <stack>

using namespace std;

typedef struct node {
	int nodeNum;
	vector<pair<int, int>> v;
}Node;

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

	// init node
	for (int i = 0; i < N; i++)
		nodeInfo[i].nodeNum = i;

	// get path info
	for (int i = 0; i < N - 1; i++) {
		int a, /* == a room linked by the path*/
			b, /* == a room linked by the path*/
			weight /* == length of the path */;

		scanf("%d %d %d", &a, &b, &weight);
		// the index started on 0
		nodeInfo[a - 1].v.push_back(make_pair(b - 1, weight));
		nodeInfo[b - 1].v.push_back(make_pair(a - 1, weight));
	}

	// finde path using DFS
	stack<Node> s;
	s.push(nodeInfo[A]);
	while (s.top().nodeNum != B) {
		// ���� ��忡�� �߰������� Ž���� ��ΰ� ���ٸ�
		// ��, ���� ��带 �����ϴ� A���� B�� �̵��ϴ� ��ΰ� �������� �ʴ´ٸ�
		if (s.top().v.empty()) {
			s.pop();
			s.top().v.pop_back();
			continue;
		}

		// ���� ��忡�� �߰������� Ž���� ��ΰ� �ִٸ�
		// ��, ���� ��带 �����ϴ� A���� B�� �̵��ϴ� ��ΰ� ������ ���ɼ��� �ִٸ�
		// ���� ��带 Ž��
		int nextNode = s.top().v.back().first;

		// �켱, ���� �ǵ��ư��°��� ����
		// ���� ���� ����� �� ��Ͽ��� ���� ���� �̾����� ���� ����
		for (vector<pair<int, int>>::iterator it = nodeInfo[nextNode].v.begin(); it != nodeInfo[nextNode].v.end(); it++) {
			if ((*it).first == s.top().nodeNum) {
				nodeInfo[nextNode].v.erase(it);
				break;
			}
		}

		// ���� ��带 ��ο� �߰�
		s.push(nodeInfo[nextNode]);
	}

	// calcualte result
	unsigned long long result = 0;
	int longest = 0;
	s.pop();
	while (!s.empty()) {
		int distance = s.top().v.back().second;
		s.pop();

		longest = (longest > distance) ? longest : distance;
		result += distance;
	}

	result -= longest;
	printf("%llu", result);

	return 0;
}