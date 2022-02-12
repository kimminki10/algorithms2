#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long ll;

void solve() {
    char c[16];
    int o = 0, x = 0;
    scanf(" %s", c);
    for (int i = 0; c[i] != '\0'; i++) {
        if (c[i] == 'o') o += 1;
        if (c[i] == 'x') x += 1;
        if (o >= 8) {
            printf("YES\n"); return;
        }
        if (x >= 8) {
            printf("NO\n"); return;
        }
    }
    if (x < 8) {
        printf("YES\n"); return;
    } else {
        printf("NO\n"); return;
    }
}

void testcase(int tc) {
    printf("#%d ", tc);
    solve();
}

int main() {
    freopen("../input.txt", "r", stdin);
    setbuf(stdout, nullptr);
    int T; scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}