/*
#2020년 1월 14일
#작성자 : 우이산
#2013년 중등부 3번 문제
#시간초과로 인한 실패
*/

#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct stick {
	int t = -1;
	int d = -1;

	unsigned long long resultToDown = -1;
	unsigned long long resultToUp = -1;
}Stick;

unsigned long long calculateToDown(vector<Stick>::iterator now, vector<Stick>::iterator s);
unsigned long long calculateToUp(vector<Stick>::iterator now, vector<Stick>::iterator s);

vector<Stick> upperLine;
vector<Stick> bottomLine;

int N;
int L;

int main() {
	scanf("%d %d", &N, &L);

	// get stick information
	for (int i = 0; i < N; i++) {
		Stick input;
		scanf("%d %d", &input.t, &input.d);

		upperLine.push_back(input);
		bottomLine.push_back(input);
	}

	// sorting line
	sort(upperLine.begin(), upperLine.end(), [](const Stick& s1, const Stick& s2)->bool {
		return s1.t < s2.t;
		});
	sort(bottomLine.begin(), bottomLine.end(), [](const Stick& s1, const Stick& s2)->bool {
		return s1.d < s2.d;
		});

	// get result
	unsigned long long result = 0;
	for (vector<Stick>::iterator it = upperLine.begin(); it != upperLine.end(); it++) {
		calculateToDown(it, bottomLine.begin());
		result = (result > (*it).resultToDown) ? result : (*it).resultToDown;
	}

	for (vector<Stick>::iterator it = bottomLine.begin(); it != bottomLine.end(); it++) {
		calculateToUp(it, upperLine.begin());
		result = (result > (*it).resultToUp) ? result : (*it).resultToUp;
	}

	printf("%llu\n", result);

	return 0;
}

unsigned long long calculateToDown(vector<Stick>::iterator now, vector<Stick>::iterator s) {
	// already calculated is ended
	if ((*now).resultToDown != -1)
		return (*now).resultToDown;

	int itselfLen = L;
	if ((*now).t > (*now).d)
		itselfLen += (*now).t - (*now).d;
	else
		itselfLen += (*now).d - (*now).t;

	(*now).resultToDown = itselfLen;

	// calcualte result
	for (; s != bottomLine.end(); s++) {
		if((*s).d == (*now).d)
			break;
	}

	if (s == bottomLine.end())
		return (*now).resultToDown;

	for ( ;s != bottomLine.end() ; s++) {
		if ((*s).d != (*now).d)
			break;

		if ((*now).t >= (*s).t) 
			continue;

		unsigned long long temp = calculateToUp(s, now) + itselfLen;
		(*now).resultToDown = ((*now).resultToDown > temp) ? (*now).resultToDown : temp;
	}

	return (*now).resultToDown;
}

unsigned long long calculateToUp(vector<Stick>::iterator now, vector<Stick>::iterator s) {
	// already calculated is ended
	if ((*now).resultToUp != -1)
		return (*now).resultToUp;

	int itselfLen = L;
	if ((*now).t > (*now).d)
		itselfLen += (*now).t - (*now).d;
	else
		itselfLen += (*now).d - (*now).t;

	(*now).resultToUp = itselfLen;

	// calcualte result
	for (; s != upperLine.end() ; s++) {
		if ((*s).t == (*now).t)
			break;
	}

	if (s == upperLine.end())
		return (*now).resultToUp;

	for (;s != upperLine.end() ; s++) {
		if ((*s).t != (*now).t)
			break;

		if ((*now).d >= (*s).d)
			continue;

		unsigned long long temp = calculateToDown(s, now) + itselfLen;
		(*now).resultToUp = ((*now).resultToUp > temp) ? (*now).resultToUp : temp;
	}

	return (*now).resultToUp;
}