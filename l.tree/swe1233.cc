#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long ll;

int solve() {
    int result = 1;
    int N;
    scanf("%d", &N);

    char line[100];
    for (int i = 0; i < N; i++) {
        scanf(" %[^\n]", line);
        int idx, left=-1, right=-1; char op='\0';
        sscanf(line, "%d %c %d %d", &idx, &op, &left, &right);

        if (idx <= N/2) {
            if ('0' <= op && op <= '9') { result = 0; }
        } else {
            if (!('0' <= op && op <= '9')) { result = 0; }
        }
    }
    return result;
}

void testcase(int tc) {
    int result = solve();
    printf("#%d %d\n", tc, result);
}

int main() {
    freopen("../input.txt", "r", stdin);

    int T; T = 10;
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}