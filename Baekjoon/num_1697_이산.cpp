#include <cstdio>
#include <queue>

using namespace std;

int main() {
	int start, dest;

	scanf("%d %d", &start, &dest);

	if (start >= dest) {
		printf("%d\n", start - dest);
		return 0;
	}

	bool* visit = new bool[dest+1];
	for (int i = 0; i < dest+1; i++)
		visit[i] = false;
	int rightSide = 200000;

	queue<int> q;
	int result = 0;
	q.push(start);
	visit[start] = true;
	while (true) {
		int r = q.size();
		for (int i = 0; i < r; i++) {
			int now = q.front();
			q.pop();

			if (now == dest) {
				printf("%d\n", result);

				delete[] visit;
				return 0;
			}

			if (now - 1 >= 0) {
				if (now - 1 < dest) {
					if (visit[now - 1] == false) {
						q.push(now - 1);
						visit[now - 1] = true;
					}
				}
				else if (now - 1 < rightSide) {
					rightSide = now - 1;
					q.push(now - 1);
				}
			}
			
			if (now + 1 <= dest && visit[now + 1] == false) {
				q.push(now + 1);
				visit[now + 1] = true;
			}
			
			if (now * 2 <= dest) {
				if (visit[now * 2] == false) {
					q.push(now * 2);
					visit[now * 2] = true;
				}
			}
			else if (now * 2 < rightSide) {
				rightSide = now * 2;
				q.push(now * 2);
			}
		}
		result++;
	}
}