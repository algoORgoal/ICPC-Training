#include <cstdio>
#include <set>
#include <queue>

using namespace std;

int main() {
	int n, m;
	scanf("%d %d", &n, &m);

	// make adjacency list
	set<int>* nodeArr = new set<int>[n];
	for (int i = 0; i < m; i++) {
		int temp1, temp2;
		scanf("%d %d", &temp1, &temp2);

		nodeArr[temp1 - 1].insert(temp2 - 1);
		nodeArr[temp2 - 1].insert(temp1 - 1);
	}

	// the number of bfs(even dfs also) is equal the number of a linked graph
	int result = 0;
	set<int> check;
	for (int s = 0; s < n; s++) {
		if (check.find(s) != check.end())
			continue;

		queue<int> bfs;
		bfs.push(s);
		check.insert(s);
		while (!bfs.empty()) {
			int now = bfs.front();
			bfs.pop();

			for (set<int>::iterator it = nodeArr[now].begin(); it != nodeArr[now].end(); it++) {
				if (check.find(*it) != check.end())
					continue;

				bfs.push(*it);
				check.insert(*it);
			}
		}
		result++;
	}

	printf("%d\n", result);

	return 0;
}