#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int n = 0;
	scanf("%d", &n);

	vector<int> lope;
	for (int i = 0; i < n; i++) {
		int temp;
		scanf("%d", &temp);
		lope.push_back(temp);
	}

	sort(lope.begin(), lope.end(), [](const int& a, const int& b) -> bool {return a > b;});

	unsigned long long result = 0;
	for (int i = 0; i < n; i++) {
		unsigned long long temp;
		temp = (i + 1) * lope.at(i);
		result = (result > temp) ? result : temp;
	}

	printf("%llu\n", result);

	return 0;
}