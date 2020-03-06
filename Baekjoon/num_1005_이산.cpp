#include <cstdio>
#include <set>

using namespace std;

typedef struct Node {
	set<int> s;
	int weight;
};

Node* arr;
int* dp;
int calculate(const set<int>::iterator& start, const set<int>::iterator& end, const int& w);

int main() {
	// the number of test case
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int n /* == N */, c /* == k*/;
		scanf("%d %d", &n, &c);

		arr = new Node[n];
		dp = new int[n];
		// get D
		for (int j = 0; j < n; j++) {
			scanf("%d", &arr[j].weight);
			dp[j] = -1;
		}

		// get order
		for (int j = 0; j < c; j++) {
			int temp1, temp2;
			scanf("%d %d", &temp1, &temp2);
			temp1--;
			temp2--;

			arr[temp2].s.insert(temp1);
		}

		int wanted/* == W*/;
		scanf("%d", &wanted);
		wanted--;

		printf("%d\n", calculate(arr[wanted].s.begin(), arr[wanted].s.end(), arr[wanted].weight));
	}

	delete[] arr;
	delete[] dp;
	return 0;
}

int calculate(const set<int>::iterator& start, const set<int>::iterator& end, const int& w) {
	int result = 0;
	for (set<int>::iterator it = start; it != end; it++) {
		int temp;
		if (dp[(*it)] == -1) {
			temp = calculate(arr[(*it)].s.begin(), arr[(*it)].s.end(), arr[(*it)].weight);
			dp[(*it)] = temp;
		}
		else {
			temp = dp[(*it)];
		}
		result = (result > temp) ? result : temp;
	}
	result += w;
	return result;
}