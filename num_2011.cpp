/*
#2020�� 1�� 15��
#2011�� ����
#�ۼ��� : ���̻�
#�ۼ���� : c++
#note
#DP �⺻����
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

	// ��� �迭 -1�� �ʱ�ȭ
	for (int i = 0; i < size; i++)
		result[i] = -1;

	printf("%d\n", calculate(0));

	return 0;
}

const int& calculate(const int& index) {
	// �̹� ���� ���
	if (result[index] != -1)
		return result[index];

	// �ؼ��� �� ���� ��ȣ���� ���
	if(arr[index] == '0')
		result[index] =  0;
	// ������ ������ ���
	else if (index == size - 1)   
		result[index] = 1;
	// �ڿ� ���ڰ� 1�� ���� ���
	else if (index == size - 2) { 
		if (arr[index] == '1' || ( arr[index] == '2' && arr[index + 1] <= '6') )
			result[index] = 1 + calculate(index + 1);
		else
			result[index] = calculate(index + 1);
	}
	// �ڿ� ���ڰ� 2�� �̻� ���� ���
	else { 
		if (arr[index] == '1' || (arr[index] == '2' && arr[index + 1] <= '6'))
			result[index] = (calculate(index + 1) + calculate(index + 2)) % 1000000;
		else
			result[index] = calculate(index + 1) % 1000000;
	}

	return result[index];
}