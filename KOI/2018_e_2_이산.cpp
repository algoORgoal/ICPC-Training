/*
#2019 12 27 ���̻�
#�ѱ������ø��ǾƵ� 2018�� �ʵ�� 2�� ����
#�־��� �׽�Ʈ ���̽� 2���� �����ϳ� 'Ʋ�Ƚ��ϴ�'
#�����׽�ũ 1���� ������Ű�� ���ϴ� ��Ȳ
*/

#include <cstdio>

// �� ������ ������ ����ü
typedef struct dot {
	int node;
	int color;
}Dot;

// ���� ��ġ�� �������� ����
void QuickSort(const int& low, const int& high, Dot*& arr);

int main() {
	int N = 0;
	scanf("%d", &N);

	// �� ���� �Է¹���
	Dot* arr = new Dot[N];
	for (int i = 0; i < N; i++) {
		int tempNode, tempColor;
		scanf("%d %d", &tempNode, &tempColor);

		arr[i].node = tempNode;
		arr[i].color = tempColor;
	}

	// �� ����
	QuickSort(0, N - 1, arr);

	// �� �������� �ٸ� �������� �ִܰŸ��� ������ �迭
	unsigned long* lenArr = new unsigned long[N];
	// �ڽź��� �����ʿ� �ִ� �� Ž��
	for (int i = 0; i < N; i++) {
		int tc = arr[i].color;
		int tn = arr[i].node;
		for (int j = i + 1; j < N; j++) {
			if (arr[j].color == tc) {
				lenArr[i] = arr[j].node - tn;
				break;
			}
			else if (j == N - 1) {
				lenArr[i] = 0;
				break;
			}
		}
	}
	// �ڽź��� ���ʿ� �ִ� �� Ž��
	for (int i = N - 1; i >= 0; i--) {
		int tc = arr[i].color;
		int tn = arr[i].node;
		for (int j = i - 1; j >= 0; j--) {
			if (arr[j].color == tc) {
				if (lenArr[i] == 0) {
					lenArr[i] = tn - arr[j].node;
					break;
				}
				else if ((tn - arr[j].node) != 0) {
					lenArr[i] = (lenArr[i] < (tn - arr[j].node)) ? lenArr[i] : (tn - arr[j].node);
					break;
				}
			}
		}
	}
	
	// ��� ���� �� ���
	unsigned long long result = 0;
	for (int i = 0; i < N; i++) {
		result += lenArr[i];
	}

	printf("%llu\n", result);

	return 0;
}

void QuickSort(const int& low, const int& high, Dot*& arr) {
	// sort is end
	if (low >= high)
		return;

	// pivot is a most right element of the array
	const int pivot = arr[high].node;

	int pi /*== pivot index */ = low;
	for (int i = low; i < high; i++) {
		if (arr[i].node < pivot) {
			// swap arr[pi] and arr[i]
			Dot temp = arr[pi];
			arr[pi] = arr[i];
			arr[i] = temp;

			pi++;
		}
	}
	// move pivot to correct position
	Dot temp = arr[pi];
	arr[pi] = arr[high];
	arr[high] = temp;

	QuickSort(low, pi - 1, arr);
	QuickSort(pi + 1, high, arr);
};