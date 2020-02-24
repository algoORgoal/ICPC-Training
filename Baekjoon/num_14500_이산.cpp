#include<cstdio>

// 래퍼런스형을 인수로 사용하지 않으면
// 제대로 된 결과가 도출된다.
// 하지만 어째서 래퍼런스형을 사용하면
// 안 되는가.
// 틀린 값도 틀린 값이지만
// 백준에선 아예 런타임 에러가 나온다

int getMax(int a, int b);
int getMax(int a, int b, int c);
int getMax(int a, int b, int c, int d);
int getMax(int a, int b, int c, int d, int e);

int getSquare(int y, int x);
int getVertical(int y, int x);
int getHorizontal(int y, int x);

int width, height;
int** map;

int main() {
	scanf("%d %d", &height, &width);

	map = new int* [height];
	for (int y = 0; y < height; y++) {
		map[y] = new int[width];
		for (int x = 0; x < width; x++) {
			int input;
			scanf("%d", &input);

			map[y][x] = input;
		}
	}

	int result = 0;
	for (int y = 0; y < height; y++) {
		for (int x = 0; x < width; x++) {
			result = getMax(getVertical(y, x), getHorizontal(y, x), getSquare(y, x), result);
		}
	}

	printf("%d\n", result);

	for (int y = 0; y < height; y++)
		delete[] map[y];
	delete[] map;

	return 0;
}

int getMax(int a, int b) {
	return (a > b) ? a : b;
}
int getMax(int a, int b, int c) {
	int temp = getMax(a, b);
	return (temp > c) ? temp : c;
}
int getMax(int a, int b, int c, int d) {
	int temp = getMax(a, b, c);
	return (temp > d) ? temp : d;
}
int getMax(int a, int b, int c, int d, int e) {
	int temp = getMax(a, b, c, d);
	return (temp > e) ? temp : e;
};

int getSquare(int y, int x) {
	int result = 0;
	if (y + 1 < height && x + 1 < width) {
		result = map[y][x] + map[y + 1][x] + map[y][x + 1] + map[y + 1][x + 1];
	}

	return result;
};
int getVertical(int y, int x) {
	int three = 0;
	int fourth = 0;

	if (y + 2 < height) {
		three = map[y][x] + map[y + 1][x] + map[y + 2][x];

		if (y > 0)
			fourth = getMax(fourth, map[y - 1][x]);

		if (x > 0)
			fourth = getMax(fourth, map[y][x - 1], map[y + 1][x - 1], map[y + 2][x - 1]);

		if (x + 1 < width)
			fourth = getMax(fourth, map[y][x + 1], map[y + 1][x + 1], map[y + 2][x + 1]);

		if (y + 3 < height)
			fourth = getMax(fourth, map[y + 3][x]);
	}

	int result = three + fourth;

	if (y + 1 < height && x > 0 && x + 1 < width)
		result = getMax(result, map[y][x] + map[y + 1][x] + getMax(map[y][x - 1] + map[y + 1][x + 1], map[y][x + 1] + map[y + 1][x - 1]));

	return result;
};
int getHorizontal(int y, int x) {
	int three = 0;
	int fourth = 0;

	if (x + 2 < width) {
		three = map[y][x] + map[y][x + 1] + map[y][x + 2];

		if (x > 0)
			fourth = getMax(fourth, map[y][x - 1]);

		if (y > 0)
			fourth = getMax(fourth, map[y - 1][x], map[y - 1][x + 1], map[y - 1][x + 2]);

		if (y + 1 < height)
			fourth = getMax(fourth, map[y + 1][x], map[y + 1][x + 1], map[y + 1][x + 2]);

		if (x + 3 < width)
			fourth = getMax(fourth, map[y][x + 3]);
	}

	int result = three + fourth;

	if (x + 1 < width && y > 0 && y + 1 < height)
		result = getMax(result, map[y][x] + map[y][x+1] + getMax(map[y+1][x] + map[y - 1][x + 1], map[y-1][x] + map[y + 1][x + 1]));
	return result;
};