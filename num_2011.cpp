/*
#2020년 1월 15일
#2011번 문제
#작성자 : 우이산
#작성언어 : c++
#note
#DP 기본문제
*/

#include <cstdio>

int size = 0;
char arr[5000];
int result[5000];

const int& calculate(const int& index);

int main() {
	for (size = 0; size < 5000; size++) {
		char temp = getchar();
		if (temp == EOF)
			break;

		arr[size] = temp;
	}

	// 결과 배열 -1로 초기화
	for (int i = 0; i < size; i++)
		result[i] = -1;

	printf("%d\n", calculate(0));

	return 0;
}

const int& calculate(const int& index) {
	// 이미 계산된 경우
	if (result[index] != -1)
		return result[index];

	// 해석할 수 없는 암호문인 경우
	if(arr[index] == '0')
		result[index] =  0;
	// 마지막 숫자인 경우
	else if (index == size - 1)   
		result[index] = 1;
	// 뒤에 숫자가 1개 남은 경우
	else if (index == size - 2) { 
		if (arr[index] == '1' || ( arr[index] == '2' && arr[index + 1] <= '6') )
			result[index] = 1 + calculate(index + 1);
		else
			result[index] = calculate(index + 1);
	}
	// 뒤에 숫자가 2개 이상 남은 경우
	else { 
		if (arr[index] == '1' || (arr[index] == '2' && arr[index + 1] <= '6'))
			result[index] = (calculate(index + 1) + calculate(index + 2)) % 1000000;
		else
			result[index] = calculate(index + 1) % 1000000;
	}

	return result[index];
}