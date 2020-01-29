#include <cstdio>

int main() {
	unsigned long long n, m;

	scanf("%llu %llu", &n, &m);

	unsigned long long exponent2 = 0;
	unsigned long long exponent5 = 0;

	if (n*m == 0 || m == n) {
		printf("0\n");
		return 0;
	}

	for (unsigned long long i = 2; i <= n; i *= 2) {
		exponent2 += n / i - (n - m) / i;
		exponent2 -= m / i;
	}

	for (unsigned long long i = 5; i <= n; i *= 5) {
		exponent5 += n / i - (n - m) / i;
		exponent5 -= m / i;
	}

	printf("%llu\n", (exponent2 < exponent5) ? exponent2 : exponent5);

	return 0;
}