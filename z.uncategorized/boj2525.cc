#include <cstdio>
using LL = long long;

int main() {
    int a, b; scanf(" %d %d", &a, &b);
    int c; scanf(" %d", &c);

    int m = a * 60 + b + c;
    printf("%d %d\n", (m / 60)%24, m % 60);
}