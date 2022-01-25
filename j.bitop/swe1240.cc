#include <iostream>
#include <cstdio>

using namespace std;

int solve() {
    int n, m; cin >> n >> m;
    char c[8] = {0,};
    int result = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m/7; j++) {
            scanf("%7s", c);
            cout << c << endl;
        }
    }
    return result;
}

void testcase(int i) {
    int result = 0;
    result = solve();
    cout << "#" << (i+1) << " " << result << endl;
}

int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    for (int i = 0; i < T; i++) {
        testcase(i);
    }
}