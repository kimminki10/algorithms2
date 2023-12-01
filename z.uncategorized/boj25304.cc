#include <cstdio>

int main() {
    int X; scanf(" %d", &X);
    int N; scanf(" %d", &N);

    int sum = 0;
    for (int i = 0; i < N; i++) {
        int a, b; scanf(" %d %d", &a, &b);
        sum += a*b;
    }
    printf("%s\n", X==sum ? "Yes" : "No");
}