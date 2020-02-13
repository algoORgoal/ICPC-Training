#include <cstdio>

typedef struct node {
	struct node* next;
	int num;
	int count;
	int startNode;
}Node;

int main() {
	// get the number of test case
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		// get the number of a node
		int n;
		scanf("%d", &n);

		// get a node's information
		Node* arr = new Node[n];
		for (int j = 0; j < n; j++) {
			int temp;
			scanf("%d", &temp);
			arr[j].next = &arr[temp - 1];
			arr[j].num = j;
			arr[j].count = -1;
			arr[j].startNode = -1;
		}

		// initialize the rsult to n
		// and then subtract
		int result = n;
		Node* now;
		for (int j = 0; j < n; j++) {
			// each search shares one startNode var
			// in other words, if node have the same startNode var,
			// one search process has gone through the nodes

			// if already searched
			if (arr[j].startNode != -1)
				continue;

			// the count var records how many times the node was located during the search
			int count = 0;
			now = &arr[j];
			now->count = count;
			now->startNode = j;

			while (now->next->startNode == -1) {
				now = now->next;
				now->count = ++count;
				now->startNode = j;
			}

			if (now->startNode == now->next->startNode) {
				result -= now->count - now->next->count + 1;
			}
		}

		printf("%d\n", result);
	}

	return 0;
}