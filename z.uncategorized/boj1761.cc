#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

const int MAX = 16;
const int MAX_N = 40'004;
int N, M;
int parent[MAX_N][MAX];
int depth[MAX_N];
vector<pair<int, int> > adj[MAX_N];
int dist[MAX_N];

void dfs(int curr) {
    for (auto p: adj[curr]) {
        int next = p.first;

        if (depth[next] == -1) {
            int v = p.second;

            depth[next] = depth[curr] + 1;
            parent[next][0] = curr;
            dist[next] = dist[curr] + v;
            dfs(next);
        }
    }
}

int lca(int a, int b) {
    if (depth[a] < depth[b]) swap(a, b);
    int diff = depth[a] - depth[b];

    for (int i = 0; diff; i++) {
        if (diff%2) a = parent[a][i];
        diff /= 2;
    }

    if (a != b) {
        for (int i=MAX-1; i>=0; i--) {
            if (parent[a][i] != -1 && parent[a][i] != parent[b][i]) {
                a = parent[a][i];
                b = parent[b][i];
            }
        }
        a = parent[a][0];
    }

    return a;
}

void init() {
    memset(parent, -1, sizeof(parent));
    fill(depth, depth+N, -1);
    fill(dist, dist+N, 0);
}

void solve() {
    scanf("%d", &N);
    for (int i = 0; i < N-1; i++) {
        int a, b, v; scanf("%d %d %d", &a, &b, &v);
        a--, b--;
        adj[a].push_back({b, v});
        adj[b].push_back({a, v});
    }
    
    init();
    depth[0] = 0;
    dfs(0);

    for (int j = 0; j < MAX-1; j++) {
        for (int i = 1; i < N; i++) {
            if (parent[i][j] != -1) {
                parent[i][j+1] = parent[ parent[i][j] ][j];
            }
        }
    }

    scanf("%d", &M);
    for (int i = 0; i < M; i++) {
        int a, b; scanf("%d %d", &a, &b);
        a--, b--;
        int w = lca(a,b);

        int result = dist[a]+dist[b] - 2*dist[w];
        printf("%d\n", result);
    }
}

int main() {
    freopen("../input.txt", "r", stdin);
    solve();
}