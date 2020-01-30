#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int n;
	scanf("%d", &n);

	vector<unsigned long> origin;
	for (int i = 0; i < n; i++) {
		unsigned long temp;
		scanf("%lu", &temp);
		origin.push_back(temp);
	}

	vector<unsigned long> clone = origin;
	sort(clone.begin(), clone.end());

	unsigned long long result = 0;
	for (vector<unsigned long>::iterator now = clone.begin(); now != clone.end(); now++) {

		unsigned long long index = 0;
		for (vector<unsigned long>::iterator it = origin.begin(); it != origin.end(); it++) {
			if ((*it) == (*now)) {
				result += index;
				origin.erase(it);
				break;
			}
			index++;
		}
	}

	printf("%llu\n", result);

	return 0;
}