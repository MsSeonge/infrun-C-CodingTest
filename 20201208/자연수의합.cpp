#include <iostream>
using namespace std;

int a, b;

void sum(int start,int end) {
	int sum = 0;
	for (int i = start; i <= end; i++) {
		sum += i;
		cout << i;
		if (i != end)
			cout << "+";
	}
	cout << sum << endl;
}

int main() {
	cin >> a >> b;
	sum(a, b);
	return 0;
}