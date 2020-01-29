#include <list>
#include <cstdio>

using namespace std;

int main() {
	list<char> str;
	char temp;
	while ((temp = getchar()) != '\n') {
		str.push_back(temp);
	}

	list<char>::iterator it = str.end();

	int m;
	scanf("%d", &m);
	getchar();
	for (int i = 0; i < m; i++) {
		temp = getchar();
		getchar();
		switch (temp) {
		case 'L':
			if(it != str.begin())
				it--;
			break;
		case 'D':
			if(it != str.end())
				it++;
			break;
		case 'B':
			if (it != str.begin())
				it = str.erase(--it);
			break;
		case 'P':
			temp = getchar();
			getchar();
			str.insert(it, temp);
			break;
		}
	}
	
	for (it = str.begin(); it != str.end(); it++)
		printf("%c", *it);
	printf("\n");

	return 0;
}