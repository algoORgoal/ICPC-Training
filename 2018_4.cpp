/* 
#2020년 1월 8일 우이산
#2018년 초등부 4번
#적성언어 c++
*/

#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

enum direction {
	NORTH = 0,
	SOUTH = 1,
	WEST = 2,
	EAST = 3
};

typedef struct square {
	int wall[4];
	bool isWallFacesOut[4] = { false, false, false, false };
	int height;

	int x, y;
	bool checked = false;
}Square;

// return direction to open
int getDir(const Square& s);
// used to sort the vector
bool isLagerSquare(const Square* Ap, const Square* Bp);

int main() {
	int N, M, H;
	scanf("%d %d %d", &N, &M, &H);

	// declare Squares
	Square** field = new Square*[N];
	for (int y = 0; y < N; y++) {
		field[y] = new Square[M];
		for (int x = 0; x < M; x++) {
			field[y][x].height = H;
			field[y][x].x = x;
			field[y][x].y = y;
		}
	}

	// set isWallFacesOut
	for (int y = 0; y < N; y++)
		field[y][0].isWallFacesOut[WEST] = field[y][M-1].isWallFacesOut[EAST] = true;
	for (int x = 0; x < M; x++)
		field[0][x].isWallFacesOut[NORTH] = field[N - 1][x].isWallFacesOut[SOUTH] = true;

	// get wall information on Squares
	for (int y = 0; y < N + 1; y++) {
		for (int x = 0; x < M; x++) {
			int input;
			scanf("%d", &input);

			if(y != 0)
				field[y-1][x].wall[SOUTH] = input;
			if (y != N)
				field[y][x].wall[NORTH] = input;
		}
	}
	for (int y = 0; y < N; y++) {
		for (int x = 0; x < M + 1; x++) {
			int input;
			scanf("%d", &input);

			if (x != 0)
				field[y][x - 1].wall[EAST] = input;
			if (x != M)
				field[y][x].wall[WEST] = input;
		}
	}

	// set border vector
	vector<Square*> border;
	for (int x = 0; x < M; x++) {
		border.push_back(&field[0][x]);
		field[0][x].checked = true;
		border.push_back(&field[N - 1][x]);
		field[N - 1][x].checked = true;
	}
	for (int y = 1; y < N - 1; y++) {
		border.push_back(&field[y][0]);
		field[y][0].checked = true;
		border.push_back(&field[y][M - 1]);
		field[y][M - 1].checked = true;
	}

	// solve the problem
	while (!border.empty()) {
		// sorting vector
		sort(border.begin(), border.end(), isLagerSquare);

		// extract a Square
		Square* now = border.back();
		border.pop_back();

		// flushing
		now->height = now->wall[getDir(*now)];

		// update left side
		if (now->x != 0) {
			Square* temp = &field[now->y][now->x - 1];
			temp->isWallFacesOut[EAST] = true;
			
			if(temp->wall[EAST] != -1)
				temp->wall[EAST] = (temp->wall[EAST] < now->height) ? now->height : temp->wall[EAST];
			
			if (temp->checked == false) {
				border.push_back(temp);
				temp->checked = true;
			}
		}

		// update right side
		if (now->x != M-1) {
			Square* temp = &field[now->y][now->x + 1];
			temp->isWallFacesOut[WEST] = true;
			
			if(temp->wall[WEST] != -1)
				temp->wall[WEST] = (temp->wall[WEST] < now->height) ? now->height : temp->wall[WEST];
			
			if (temp->checked == false) {
				border.push_back(temp);
				temp->checked = true;
			}
		}

		// update up side
		if (now->y != 0) {
			Square* temp = &field[now->y - 1][now->x];
			temp->isWallFacesOut[SOUTH] = true;
			
			if(temp->wall[SOUTH] != -1)
				temp->wall[SOUTH] = (temp->wall[SOUTH] < now->height) ? now->height : temp->wall[SOUTH];
			
			if (temp->checked == false) {
				border.push_back(temp);
				temp->checked = true;
			}
		}

		// update down side
		if (now->y != N-1) {
			Square* temp = &field[now->y+1][now->x];
			temp->isWallFacesOut[NORTH] = true;
			
			if(temp->wall[NORTH] != -1)
				temp->wall[NORTH] = (temp->wall[NORTH] < now->height) ? now->height : temp->wall[NORTH];
			
			if (temp->checked == false) {
				border.push_back(temp);
				temp->checked = true;
			}
		}
	}

	unsigned long long result = 0;
	for (int y = 0; y < N; y++) {
		for (int x = 0; x < M; x++) {
			result += field[y][x].height;
		}
	}

	printf("%llu\n", result);

	return 0;
}

int getDir(const Square& s) {
	int direction = -1;
	for (int i = 0; i < 4; i++) {
		if (s.isWallFacesOut[i] && s.wall[i] != -1){
			if (direction == -1)
				direction = i;
			direction = (s.wall[direction] < s.wall[i]) ? direction : i;
		}
	}
	return direction;
};

bool isLagerSquare(const Square* Ap, const Square* Bp) {
	// in acmicpc.net, can't use INT_MAX value. that's why I use '9999'
	int a = (getDir(*Ap) == -1) ? 9999 : Ap->wall[getDir(*Ap)];
	int b = (getDir(*Bp) == -1) ? 9999 : Bp->wall[getDir(*Bp)];
	return a > b;
};