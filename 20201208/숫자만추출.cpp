#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;


string in;
int res = 0,cnt=0;
int main() {
	freopen("input.txt", "rt", stdin);
	cin >> in;
	for (int i = 0; i != '\n'; i++) {
		if (in[i] >= 48 && in[i] <= 57)
			res = res * 10 + (in[i] - 48);
	}
	cout << res << endl;
		for (int i = 1; i <= res; i++) { //0 error ¹ß»ý 
			if (res % i == 0)
				cnt++;
		}
		cout << cnt << endl;
	return 0;
}