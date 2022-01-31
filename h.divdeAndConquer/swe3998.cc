#include <iostream>

using namespace std;

int TN;
long long tree[100'000 * 4];

long long  range_sum(int ql, int qr, int idx=1, int l=1, int r=TN) {
    if (ql <= l && r <= qr) { return tree[idx]; }
    if (r < ql || qr < l) return 0LL;
    return range_sum(ql, qr, idx*2, l, (l+r)/2) +
           range_sum(ql, qr, idx*2+1, (l+r)/2+1, r);
}

void change_val(int idx, int val) {
    tree[idx = (TN+idx-1)] = val;
    for (idx >>= 1; idx; idx >>= 1) {
        tree[idx]=tree[idx*2] + tree[idx*2+1];
    }
}

long long solve() {
    long long  result = 0;

    int N; cin >> N;
    for(TN=1; TN < N; TN<<=1) {}
    for (int i = 1, x; i <= N; i++) {
        cin >> x;

        result += range_sum(x, N);
        change_val(x, 1);
    }

    return result;
}

void testcase(int tc) {
    for (int i = 0; i < 100'000*4; i++) { tree[i] = 0; }
    long long result = solve();
    cout << "#" << tc << " " << result << "\n";
}

int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("../inputpy.txt", "r", stdin);

    int T; cin>> T;
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}