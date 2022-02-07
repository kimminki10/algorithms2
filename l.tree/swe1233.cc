#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long ll;

struct Node {
    char c='\0';
    int l= -1, r=-1;
    Node() : Node('\0', -1, -1) {}
    Node(char ch, int le, int ri): c(ch), l(le), r(ri) {}
};

Node n[201];
int N;

void inorder(int idx) {
    Node c = n[idx];
    if (c.l != -1) inorder(c.l);
    if (c.c != '\0') printf("%c", c.c);
    if (c.r != -1) inorder(c.r);
}

int solve() {
    scanf("%d", &N);

    char line[100];
    for (int i = 0; i < N; i++) {
        scanf(" %[\n]", line);
        int idx, left=-1, right=-1; char op='\0';
        sscanf(line, "%d %c %d %d", &idx, &op, &left, &right);
    }


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