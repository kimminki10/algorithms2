#include <iostream>
#include <algorithm>

using namespace std;

int N, M; 
int arr[3'003];
int brr[102];
int d[3'003][101][101][2]; // arr 에서 확인한 수, brr에서 채워 넣고 가져간거, brr에서 채워넣고 안가져간거, arr가져간거 안가져간거

int dodo(int i, int l, int r, int t) {
    int &c = d[i][l][r][t];
    
    if (c != -1) { return c; }
    if (i == 0 && l == 0) { return c=0; }
    if (l+r > M) { return c=0; }

    if (t == 1) {
        int a = i > 0? dodo(i-1, l, r, 0) + arr[i-1] : 0;
        int b = l > 0? dodo(i, l-1, r, 0) + brr[M-l] : 0;
        c = max(a, b);
    } else {
        if (i > 0) {
            c = max(dodo(i-1, l, r, 0), 
                    dodo(i-1, l, r, 1));
        }
        if (r > 0) {
            c = max(c, dodo(i, l, r-1, 0));
            c = max(c, dodo(i, l, r-1, 1));
        }
    }

    return c;
}

int solve() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> brr[i];
    }

    for (int i = 0; i<= N; i++) {
        for (int j = 0; j <= M; j++) {
            for (int l = 0; l <= M; l++) {
                d[i][j][l][0] = -1;
                d[i][j][l][1] = -1;
            }
        }
    }
    sort(brr, brr+M);
    
    int result = 0;
    for (int l = 0; l <= M; l++) {
        int r = M-l;
        result = max(result, dodo(N, l, r, 0));
        result = max(result, dodo(N, l, r, 1));
    }
    return result;
}

void testcase(int tc) {
    int result = solve();
    cout << "#" << tc << " " << result << endl;
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