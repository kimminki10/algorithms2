#include <cstdio>

int main() {
    int N; scanf(" %d", &N);
    N = N / 4 - 1;
    printf("long");
    for (int i = 0; i < N; i++) {
        printf(" long");
    }
    printf(" int\n");
}