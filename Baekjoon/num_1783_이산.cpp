#include <cstdio>

int main() {
	unsigned long long y, x;
	scanf("%llu %llu", &y, &x);

	unsigned long long result = 0;
	if (y == 1) {
		printf("1\n");
	}
	else if (y == 2) {
		if (x > 6)
			result = 4;
		else
			result = (x-1) / 2 + 1;

		printf("%llu\n", result);
	}
	else {
		if (x > 6)
			result = (x - 5) + 3;
		else {
			result = (x - 1 > 2) ? 4 : x;
		}

		printf("%llu\n", result);
	}

	return 0;
}