#include <cstdio>
#include <queue>

using namespace std;

typedef struct node {
	int num;
	int x, y;
	bool check;
}Node;

int main() {
	int n, m;
	scanf("%d %d", &n, &m);

	int count = 0;
	Node** map = new Node*[n];
	for (int y = 0; y < n; y++) {
		map[y] = new Node[m];
		for (int x = 0; x < m; x++) {
			int temp;
			scanf("%d", &temp);

			map[y][x].num = temp;
			map[y][x].x = x;
			map[y][x].y = y;
			map[y][x].check = false;
			
			if (temp == 1)
				count++;
		}
	}

	int result = 0;
	while (count > 0) {
		queue<Node*> q;
		q.push(&map[0][0]);
		map[0][0].check = true;
		while (!q.empty()) {
			Node* now = q.front();
			q.pop();

			if (now->x != 0) {
				Node* next = &map[now->y][now->x - 1];

				if (next->num != 0) {
					next->num++;
				}
				else {
					if (next->check == false) {
						q.push(next);
						next->check = true;
					}
				}
			}
			if (now->x != m-1) {
				Node* next = &map[now->y][now->x + 1];

				if (next->num != 0) {
					next->num++;
				}
				else {
					if (next->check == false) {
						q.push(next);
						next->check = true;
					}
				}
			}
			if (now->y != 0) {
				Node* next = &map[now->y - 1][now->x];

				if (next->num != 0) {
					next->num++;
				}
				else {
					if (next->check == false) {
						q.push(next);
						next->check = true;
					}
				}
			}
			if (now->y != n-1) {
				Node* next = &map[now->y + 1][now->x];

				if (next->num != 0) {
					next->num++;
				}
				else {
					if (next->check == false) {
						q.push(next);
						next->check = true;
					}
				}
			}
		}

		for (int y = 0; y < n; y++) {
			for (int x = 0; x < m; x++) {
				map[y][x].check = false;

				if (map[y][x].num > 2) {
					map[y][x].num = 0;
					count--;
				}
				else if (map[y][x].num > 0) {
					map[y][x].num = 1;
				}
			}
		}

		result++;
	}

	printf("%d\n", result);

	return 0;
}