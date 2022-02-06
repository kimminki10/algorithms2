#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long ll;

int uf[50'001];
int find(int a) {
    if (a == uf[a]) { return a;}
    else return uf[a] = find(uf[a]);
}

bool merge(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) { return false; }
    uf[b] = a;
    return true;
}

struct Edge {
    int s, e, c;
    Edge(): Edge(-1,-1,-1) {}
    Edge(int start, int end, int cost): s(start), e(end), c(cost){}

    bool operator < (const Edge& e2) const { return c < e2.c; }
};

int N, M;
ll solve() {
    scanf("%d %d", &N, &M);
    vector<Edge> edges;

    for (int i = 0; i < M; i++) {
        int s,e,c; scanf("%d %d %d", &s, &e, &c);
        edges.push_back({s-1, e-1, c});
    }

    sort(edges.begin(), edges.end());
    for (int i = 0; i < N; i++) { uf[i] = i; }
    ll result = 0, cnt = 0;
    for (int i = 0; ; i++) {
        if (merge(edges[i].s, edges[i].e)) {
            result += edges[i].c;
            if (++cnt == N-1) { break; }
        }
    }
    return result;
}

void testcase(int tc) {
    ll result = solve();
    printf("#%d %lld\n", tc, result);
}

int main() {
    freopen("../input.txt", "r", stdin);

    int T; scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}