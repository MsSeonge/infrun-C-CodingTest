#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

string in;
char Sexual;
int year;

int main() {
	freopen("input.txt", "rt", stdin);
	cin >> in;
	if (in[7] == '1' or in[7] == '2') {
		if (in[7] == '1')
			Sexual = 'M';
		else
			Sexual = 'W';
		year = 2019 - (1900 + ((in[0] - 48) * 10+ (in[1] - 48)));
	}
	else {
		if (in[7] == '3')
			Sexual = 'M';
		else
			Sexual = 'W';
		year = 2019 - (2000 + (((in[0] - 48) * 10) + (in[1] - 48)));
	}
	cout << year+1 << " " << Sexual << endl;
	return 0;
}