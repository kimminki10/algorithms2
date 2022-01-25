#include <iostream>
#include <algorithm>

using namespace std;


int varr[101];
int carr[101];

int result = 0;
int d[101][10001];

void solve() {
    int N, k; cin >> N >> k;

    for (int i = 1; i <= N; i++) {
        cin >> varr[i] >> carr[i];
    }

    for (int i = 1; i <= N; i++) {
        for (int j = 0; j <= k; j++) {
            if (varr[i] <= j) {
                d[i][j] = max(carr[i] + d[i-1][j-varr[i]], d[i-1][j]);
            } else {
                d[i][j] = d[i-1][j];
            }
        }
    }

    result = d[N][k];
}

void testcase(int tc) {
    for (int i = 0; i < 101; i++) {
        for (int j = 0; j < 10001; j++) {
            d[i][j] = 0;
        }
    }
    result = 0;

    solve();
    cout << "#" << tc << " " << result << endl;
}
int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("../input.txt", "r", stdin);

    int T; cin >> T;
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}