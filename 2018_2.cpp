/*
#2019 12 27 우이산
#한국정보올림피아드 2018년 초등부 2번 문제
#주어진 테스트 케이스 2개는 만족하나 '틀렸습니다'
#서브테스크 1번도 충족시키지 못하는 상황
*/

#include <cstdio>

// 점 정보를 저장할 구조체
typedef struct dot {
	int node;
	int color;
}Dot;

// 점의 위치를 기준으로 정렬
void QuickSort(const int& low, const int& high, Dot*& arr);

int main() {
	int N = 0;
	scanf("%d", &N);

	// 점 정보 입력받음
	Dot* arr = new Dot[N];
	for (int i = 0; i < N; i++) {
		int tempNode, tempColor;
		scanf("%d %d", &tempNode, &tempColor);

		arr[i].node = tempNode;
		arr[i].color = tempColor;
	}

	// 점 정렬
	QuickSort(0, N - 1, arr);

	// 각 점에서의 다른 점으로의 최단거리를 저장할 배열
	unsigned long* lenArr = new unsigned long[N];
	// 자신보다 오른쪽에 있는 점 탐색
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
	// 자신보다 왼쪽에 있는 점 탐색
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
	
	// 결과 산출 및 출력
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