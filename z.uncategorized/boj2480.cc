#include <cstdio>

int nun[7] = {0,};
int main() {
    int a;
    for (int i = 0; i < 3; i++) {
        scanf(" %d", &a); nun[a]++;
    }

    int ans = 0;
    for (int i = 1; i <= 6; i++) {
        if      (nun[i] == 3) { ans = 10000 + i * 1000; break; } 
        else if (nun[i] == 2) { ans = 1000  + i * 100;  break; }
        else if (nun[i] == 1) { ans = i * 100; }
    }
    printf("%d\n", ans);
}