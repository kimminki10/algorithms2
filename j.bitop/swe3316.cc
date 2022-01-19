#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int solve() {
    int d[10'001][16] = {0,};

    string kp; // keyPerson
    cin >> kp;
    int result = 0;

    int prev = 0b1111;
    int c = (1 << (int)(kp[0] - 'A'));
    for (int i = 1; i < 16; i++) {
        if ((c & i) && (i & 1)) { d[0][i] += 1; }
    }

    for (int i = 1; i < kp.size(); i++) {
        c = (1 << (int)(kp[i] - 'A'));
        for (int j = 1; j < 16; j++) {
            if (d[i-1][j]) {
                for (int x = 1; x < 16; x++) {
                    if ((j & x) && (c & x)) {
                        d[i][x] = (d[i][x] + d[i-1][j]) % 1'000'000'007;
                    }
                }
            }
        }
    }

    for (int i = 0; i < 16; i++) {
        result = (result + d[kp.size()-1][i]) % 1'000'000'007;
    }

    return result;
}

void testcase(int tc) {
    int result = 0;
    result = solve();
    cout << "#" << (tc+1) << " " << result << endl;
}

int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);

    int TC;
    cin >> TC;
    for (int i = 0; i < TC; i++) {
        testcase(i);
    }
}