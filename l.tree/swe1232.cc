#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long ll;

struct Node {
    int op = 0;
    int l=-1, r=-1;
} node[1'001];

int eval(int idx) {
    Node n = node[idx];
    if (n.l == -1 && n.r == -1) { // is num?
        return n.op;
    } 
    if (n.op == '+') { return eval(n.l) + eval(n.r); }
    if (n.op == '-') { return eval(n.l) - eval(n.r); }
    if (n.op == '*') { return eval(n.l) * eval(n.r); }
    if (n.op == '/') { return eval(n.l) / eval(n.r); }
}

int solve() {
    int N;
    scanf("%d", &N);

    char line[100];
    for (int i = 0; i < N; i++) {
        scanf(" %[^\n]", line);
        int idx, left=-1, right=-1; int op=0;
        int re = sscanf(line, "%d %d", &idx, &op);
        if (re == 1) sscanf(line, "%d %c %d %d", &idx, &op, &left, &right);

        node[idx].op = op;
        node[idx].l = left;
        node[idx].r = right;
    }

    return eval(1);
}

void testcase(int tc) {
    int result = solve();
    printf("#%d %d\n", tc, result);
}

int main() {
    freopen("../input.txt", "r", stdin);

    int T; T=10;
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}