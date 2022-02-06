#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long ll;

struct node {
    char c = '\0';
    int l=-1, r=-1;
    node(): node('\0', -1, -1) {}
    node(char w, int left, int right): c(w), l(left), r(right){}
};
node n[101];

void inorder(int idx) {
    node c = n[idx];
    if (c.l != -1) inorder(c.l);
    if (c.c != '\0') printf("%c", c.c);
    if (c.r != -1) inorder(c.r);
}

int N;
void solve() {
    scanf("%d", &N);
    char s[400];
    for (int i = 1; i <= N; i++) {
        scanf(" %[^\n]", s);
        int a; char c; int l=-1,r=-1; 
        sscanf(s, "%d %c %d %d", &a, &c, &l, &r);

        n[a] = node(c, l, r);
    }

    inorder(1);

}

void testcase(int tc) {
    printf("#%d ", tc);
    solve();
    printf("\n");
}

int main() {
    freopen("../input.txt", "r", stdin);

    for (int i = 0; i < 10; i++) {
        testcase(i+1);
    }
}