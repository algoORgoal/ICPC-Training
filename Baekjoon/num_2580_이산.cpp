#include <cstdio>
#include <vector>

using namespace std;

typedef struct dot {
	int y;
	int x;
	int num;
}Dot;

int main() {
	Dot map[9][9] = {};
	vector<Dot*> v;
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			int temp;
			scanf("%d", &temp);

			map[i][j].y = i;
			map[i][j].x = j;
			map[i][j].num = temp;

			if (temp == 0) {
				v.push_back(&map[i][j]);
			}
		}
	}

	for (vector<Dot*>::iterator it = v.begin(); it != v.end();) {
		bool flag = true;
		
		for (int n = (*it)->num + 1 ; n < 10; n++) {
			(*it)->num = n;
			flag = false;

			for (int x = 0; x < 9; x++) {
				if (x == (*it)->x)
					continue;

				if (map[(*it)->y][x].num == n) {
					flag = true;
					break;
				}
			}

			for (int y = 0; y < 9; y++) {
				if (y == (*it)->y)
					continue;

				if (map[y][(*it)->x].num == n) {
					flag = true;
					break;
				}
			}

			int startY = (*it)->y / 3 * 3;
			int startX = (*it)->x / 3 * 3;
			for (int y = startY; y < startY + 3; y++) {
				for (int x = startX; x < startX + 3; x++) {
					if (y == (*it)->y && x == (*it)->x)
						continue;

					if (map[y][x].num == n) {
						flag = true;
						x = 10;
						y = 10;
						break;
					}
				}
			}

			if (flag == false)
				break;
		}

		if (flag == true) {
			(*it)->num = 0;
			it--;
		}
		else {

			it++;
		}
	}

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			printf("%d ", map[i][j].num);
		}
		printf("\n");
	}

	return 0;
}