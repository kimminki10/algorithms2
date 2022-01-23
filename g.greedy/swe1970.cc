#include <iostream>

using namespace std;

void testcase(int tc) {
    int N; cin >> N;
    int arr[8] = {0,};
    int money = 50'000;

    for (int i = 0; i < 8; i++) {
        if (N >= money) {
            arr[i] = N / money;
            N = N - (N/money) * money;
        }

        if (i % 2 == 0) {
            money /= 5;
        } else {
            money /= 2;
        }
    }
    cout << "#" << tc << endl;
    for (int i = 0; i < 8; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}
int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("input.txt", "r", stdin);

    int t; cin>>t;
    for (int i = 0; i < t; i++) {
        testcase(i+1);
    }
}