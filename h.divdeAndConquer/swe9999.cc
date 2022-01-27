#include <iostream>
#include <algorithm>

using namespace std;

int L, N;
int srr[100'001];
int err[100'001];
int sum[100'001];

bool isPossible(int m, int v) {
    if (srr[m] <= v) {
        return true;
    }
    return false;
}

int binarySearch(int v) {
    int l=1, r = N, ans, m;
    while (l <= r) {
        m = (l+r)/2;
        if (isPossible(m, v)) {
            ans = m;
            l = m+1;
        } else r = m-1;
    }
    return ans;
}

int solve() {
    cin >> L;
    cin >> N;

    for (int i = 1; i <= N; i++) {
        cin >> srr[i] >> err[i];
    }
    for (int i = 1; i <= N; i++)
        sum[i] = err[i] - srr[i] + sum[i-1];

    int max = 0, t;
    for (int i = 1; i <= N; i++) {
        int r_idx = binarySearch(srr[i] + L);
        t = sum[r_idx] - sum[i-1];
        if (err[r_idx] > srr[i] + L) {
            t -= err[r_idx] - (srr[i] + L);
        }
        if (t > max) max = t;
    }
    return max;
}

void testcase(int tc) {
    for (int i = 0; i < 100'001; i++) {
        err[i] = 0; srr[i] = 0; sum[i] = 0;
    }
    int result = solve();
    cout << "#" << tc << " " << result << "\n";
}

int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("../input.txt", "r", stdin);

    int T; cin>> T;
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}