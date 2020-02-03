#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	unsigned long long n;
	scanf("%llu", &n);

	vector<unsigned long long> v1;
	for (int i = 0; i < 6; i++) {
		unsigned long long temp;
		scanf("%llu", &temp);
		v1.push_back(temp);
	}

	if (n == 1) {
		sort(v1.begin(), v1.end());
		unsigned long long result = 0;
		for (int i = 0; i < 5; i++)
			result += v1.at(i);
		printf("%llu\n", result);
		return 0;
	}

	vector<unsigned long long> v2;
	v2.push_back((v1.at(0) < v1.at(5)) ? v1.at(0) : v1.at(5));
	v2.push_back((v1.at(1) < v1.at(4)) ? v1.at(1) : v1.at(4));
	v2.push_back((v1.at(2) < v1.at(3)) ? v1.at(2) : v1.at(3));
	sort(v2.begin(), v2.end());

	printf("%llu\n", v2.at(2) * 4 + v2.at(1) * (4 * n + 4 * (n - 2)) + v2.at(0) * (4 * n + 4 * (n - 2) + 5 * (n - 2) * (n - 2)));

	return 0;
}