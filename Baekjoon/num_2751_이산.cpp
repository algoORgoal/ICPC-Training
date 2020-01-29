#include <cstdio>

int n;
int* arr;

void quickSort(const int& start, const int& end);

int main() {
	scanf("%d", &n);

	arr = new int[n];

	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);

	quickSort(0, n);

	for (int i = 0; i < n; i++)
		printf("%d\n", arr[i]);

	return 0;
}

void quickSort(const int& start, const int& end) {
	int pivotIndex = start;
	const int pivotValue = arr[start];

	for (int i = start + 1; i < end; i++) {
		if (arr[i] < pivotValue) {
			pivotIndex++;
		}
		else {
			int temp = arr[pivotIndex];
			arr[pivotIndex] = arr[i];
			arr[i] = temp;
		}
	}
}