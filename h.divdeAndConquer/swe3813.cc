#include <iostream>
#include <algorithm>

using namespace std;

int N, K;
int warr[200'005];
int sarr[200'005];

bool isPossible(int m) {
    int i = 0;
    for (int ik = 0; ik < K; ik++) {
        int k = sarr[ik];
        int c = 0;
        for (; i < N; i++) {

            if (warr[i] <= m) {
                int j;
                for (j = 0; j < k && i+j < N; j++) {
                    if (warr[i+j] <= m) {
                        c++;
                    } else { break; }
                }
                i += j;
            }

            if (c == k) { break; }
            else { c = 0; }
        }

        if (ik == K-1 && c == k) { return true; }
    }

    return false;
}

int solve() {
    cin >> N >> K;
    for (int i = 0; i < N; i++) { cin >> warr[i]; }
    for (int i = 0; i < K; i++) { cin >> sarr[i]; }

    int l = 1, r = 200'000, ans, m;
    while (l <= r) {
        m = (l+r) / 2;

        if (isPossible(m)) {
            ans = m;
            r = m-1;
        } else l = m+1;
    }
    return ans;
}

void testcase(int tc) {
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