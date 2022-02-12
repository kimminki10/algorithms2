#include <cstdio>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

int N, M;
unordered_map<string, int> hashmap;
char narr[100'000][51];

void solve() { 
    scanf("%d %d", &N, &M);

    char s[51];
    for (int i = 0; i < N; i++) {
        scanf(" %s", s); 
        hashmap[string(s)] = 1;
    }

    int count = 0;
    for (int i = 0; i < M; i++) {
        scanf(" %s", s);

        int re = hashmap[string(s)];
        if (re) count++;
    }

    printf("%d\n", count);
}

void testcase(int tc) {
    hashmap = {};
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