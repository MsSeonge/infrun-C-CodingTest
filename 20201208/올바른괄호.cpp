#include <iostream>
using namespace std;

string in;
int cnt = 0;
int main(){
	cin >> in;
	for (int i = 0; in[i] != '\0'; i++) {
		if (in[i] == '(')
			cnt++;
		else {
			cnt--;
			if (cnt != 0) {
				cout << "NO" << endl;
				return 0;
			}
		}
	}
	if (cnt > 0)
		cout << "NO" << endl;
	else
		cout << "YES" << endl;
	return 0;
}
