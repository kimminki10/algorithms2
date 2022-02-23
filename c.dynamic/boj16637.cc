#include <cstdio>
#include <algorithm>
#include <ctime>
#include <climits>
using namespace std;

int num[21]; int numsz=0;
char op[21]; int opsz=0;
int result = INT_MIN;

int eval(int a, int b, char op) {
    if (op == '+') { return a+b; }
    if (op == '-') { return a-b; }
    if (op == '*') { return a*b; }
    
    return 0;
}

void go(int i, int cur) {
    if (i >= opsz) { 
        result = max(cur, result);
        return; 
    }
    go(i+1, eval(cur, num[i+1], op[i]));

    if (i == opsz-1) { return; }
    int next = eval(num[i+1], num[i+2], op[i+1]);
    go(i+2, eval(cur, next, op[i]));
}

int main() {
    freopen("../input.txt", "r", stdin);
    int N; scanf("%d", &N);
    char line[20]; scanf("%s", line);

    op[opsz++] = '+';
    num[numsz++] = 0;
    for (int i = 0; i < N; i++) {
        if (i%2) { op[opsz++]   = line[i]; }
        else     { num[numsz++] = line[i] - '0';}
    }
    go(0, 0);
    printf("%d\n", result);
}