#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int uf[1'000];
int find(int a) {
    if (a == uf[a]) { return a; }
    else { return uf[a] = find(uf[a]); }
}

bool merge(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) { return false; }
    uf[b] = a; 
    return true;
}

class Edge {
    public:
    int u,v,w;
    Edge(): Edge(-1,-1,0) {}
    Edge(int a, int b, int c): u(a), v(b), w(c) {}
    bool operator < (const Edge& e) const { return w < e.w; }
};
int N, M;
void solve() {
    scanf("%d %d", &N, &M);
    Edge e[100'000];

    for (int i = 0; i < M; i++) {
        int a, b, c; scanf("%d %d %d", &a, &b, &c);
        e[i] = Edge(a-1, b-1, c);
    }

    sort(e, e+M);

    for (int i = 0; i < N; i++) { uf[i] = i; }
    int result = 0, cnt = 0;
    for (int i = 0; ; i++) {
        if (merge(e[i].u, e[i].v)) {
            result += e[i].w;
            if (++cnt == N-1) break;
        }
    }
    printf("%d\n", result);
}

int main() {
    freopen("../input.txt", "r", stdin);
    solve();
}