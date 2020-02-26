#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int n;
	scanf("%d", &n);
	
	vector<int> v;
	for (int i = 0; i < n; i++) {
		int input;
		scanf("%d", &input);
		v.push_back(input);
	}

	sort(v.begin(), v.end());

	unsigned long long result = 0;
	for (vector<int>::iterator it = v.begin(); it != v.end(); it++) {
		if (it + 1 == v.end()) {
			result += *it;
			v.erase(it);
			break;
		}
		else if (*it <= 0 && *(it+1) <= 0) {
			result += *it + *(it+1);
			it = v.erase(it, it+2);
		}
		else {
			break;
		}
	}
	reverse(v.begin(), v.end());

	for (vector<int>::iterator it = v.begin(); it != v.end(); it++) {
		if (it + 1 == v.end()) {
			result += *it;
			v.erase(it);
			break;
		}
		else if (*it >= 0 && *(it + 1) >= 0) {
			result += *it + *(it + 1);
			it = v.erase(it, it + 2);
		}
		else {
			break;
		}
	}

	printf("%llu\n", result);

	return 0;
}