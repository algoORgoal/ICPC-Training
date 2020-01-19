  /*
#2019/1/1 우이산
#2018년 초등부 3번 문제
#작성언어 c++
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
		// 현재 노드에서 추가적으로 탐색할 경로가 없다면
		// 즉, 현재 노드를 경유하는 A에서 B로 이동하는 경로가 존재하지 않는다면
		if (s.top().v.empty()) {
			s.pop();
			s.top().v.pop_back();
			continue;
		}

		// 현재 노드에서 추가적으로 탐색할 경로가 있다면
		// 즉, 현재 노드를 경유하는 A에서 B로 이동하는 경로가 존재할 가능성이 있다면
		// 다음 노드를 탐색
		int nextNode = s.top().v.back().first;

		// 우선, 길을 되돌아가는것을 방지
		// 다음 노드와 연결된 길 목록에서 현재 노드와 이어지는 길을 제거
		for (vector<pair<int, int>>::iterator it = nodeInfo[nextNode].v.begin(); it != nodeInfo[nextNode].v.end(); it++) {
			if ((*it).first == s.top().nodeNum) {
				nodeInfo[nextNode].v.erase(it);
				break;
			}
		}

		// 다음 노드를 경로에 추가
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