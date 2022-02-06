#include <cstdio>
#include <cstring>
#include <climits>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long ll;

double E;
int N;
int xarr[1'001], yarr[1'001];

int uf[1'000];
int find(int a) {
    if (a == uf[a]) { return a; }
    else { return uf[a] = find(uf[a]); }
}

bool sameRoot(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) { return false; }
    uf[b] = a; 
    return true;
}

class Edge {
    public:
    int u;
    int v;
    ll w;
    Edge():Edge(-1,-1,0){}
    Edge(int a, int b, ll c): u(a), w(c), v(b){}

    bool operator < (const Edge n) const { return w < n.w; }
};

inline ll ecoPay(ll x, ll y, ll a, ll b) {
    return (x-a) * (x-a) + (y-b) * (y-b);
}

ll solve() {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) { scanf("%d", &xarr[i]); }
    for (int i = 0; i < N; i++) { scanf("%d", &yarr[i]); }

    scanf("%lf", &E);
    vector<Edge> e;
    for (int i = 0; i < N; i++) {
        for (int j = i+1; j < N; j++) {
            ll epay = ecoPay(xarr[i], yarr[i], xarr[j], yarr[j]);
            e.push_back({i, j, epay});
        }
    }

    for (int i = 0; i < N; i++) { uf[i] = i; }
    sort(e.begin(), e.end());
    ll result = 0; int cnt = 0;
    for (int i = 0; ;i++) {
        if (sameRoot(e[i].u, e[i].v)) {
            result += e[i].w;
            if (++cnt == N-1) { break; }
        }
    }

    return result * E + 0.5;
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