#include <cstdio>
#include <vector>
#include <utility>

using namespace std;

int main() {
	int t, k;
	scanf("%d %d", &t, &k);

	vector<pair<int, int>> v;
	for (int i = 0; i < k; i++) {
		int price, amount;
		scanf("%d %d", &price, &amount);

		v.push_back(make_pair(price, amount));
	}

	unsigned long long* dp = new unsigned long long[t+1];
	for (int i = 0; i < t+1; i++) {
		dp[i] = 0;
	}

	for (vector<pair<int, int>>::iterator it = v.begin(); it != v.end(); it++) {
		int e = (*it).first;
		int n = (*it).second;

		unsigned long long* copy = new unsigned long long[t + 1];
		for (int i = 0; i < t + 1; i++) {
			copy[i] = dp[i];
		}

		for (int i = 1; i < t+1; i++) {
			if (i % e == 0 && i / e <= n)
				dp[i]++;

			if (copy[i] != 0) {
				for (int j = 1; j < n + 1; j++) {
					if (i + e * j >= t + 1) {
						break;
					}

					dp[i + e * j] += copy[i];
				}
			}
		}
		delete[] copy;
	}

	printf("%llu\n", dp[t]);

	delete[] dp;
	return 0;
}