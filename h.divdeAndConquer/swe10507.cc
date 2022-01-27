#include <iostream>

using namespace std;

int n, p;
int arr[200'005] = {0,};
short int srr[1'000'006] = {0,};

bool isPossible(int len) {
    int i = 0, j = len;
    if (srr[0] == 1 && srr[j] + p >= len) {
        return true;
    } 
    for (; i <= 1'000'000 && j <= 1'000'000; i++, j++) {
        if (srr[j] - srr[i] + p >= len) {
            return true;
        }
    }
    return false;
}

int solve() {
    cin >> n >> p;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        srr[arr[i]] = 1;
    }

    for (int i = 1; i <= 1'000'000; i++) {
        srr[i] += srr[i-1];
    }

    int l = 0, r = n+p, ans, m;
    while (l <= r) {
        m = (l + r) / 2;
        if (isPossible(m)) {
            ans = m;
            l = m + 1;
        } else {
            r = m - 1;
        }
    }

    return ans;
}

void testcase(int tc) {
    for (int i = 0; i < 200'005; i++) { arr[i] = 0; }
    for (int i = 0; i < 1'000'006; i++) { srr[i] = 0; }
    int result = solve();
    cout << "#" << tc << " " << result << "\n";
}

int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("../input.txt", "r", stdin);

    int T; cin >> T;
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}