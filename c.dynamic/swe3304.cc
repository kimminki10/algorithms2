#include <iostream>
#include <algorithm>

using namespace std;

int d[1003][1003] = {0,};
int solve() {
    int result = 0;
    string sa, sb; 
    cin >> sa;
    cin >> sb;

    int i, j;

    for (i = 1; sa[i-1]; i++) {
        for (j = 1; sb[j-1]; j++) {
            if (sa[i-1] == sb[j-1]) {
                d[i][j] = d[i-1][j-1] + 1;
            } else {
                d[i][j] = max(d[i][j-1], d[i-1][j]);
            }
        }
    }
    
    result = d[i-1][j-1];
    return result;
}

void testcase(int tc) {
    for (int i = 0; i < 1001; i++) {
        for (int j = 0; j < 1001; j++) {
            d[i][j] = 0;
        }
    }
    int result = solve();
    cout << "#" << tc << " " << result << endl;
}

int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("../input.txt", "r", stdin);

    int T; cin>> T;
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}