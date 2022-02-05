#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const int MAX = 18;
int N;
int depth[100'005];
int parent[100'005][MAX];
vector<int> adj[100'005];

int lca(int a, int b) {
    if (depth[a] < depth[b]) swap(a, b);
    int diff = depth[a] - depth[b];

    for (int j=0; diff; j++) {
        if (diff%2) a = parent[a][j];
        diff /= 2;
    }

    if (a != b) {
        for (int j=MAX-1; j>=0; j--) {
            if (parent[a][j] != -1 && parent[a][j] != parent[b][j]) {
                a = parent[a][j];
                b = parent[b][j];
            }
        }
        a = parent[a][0];
    }
    return a;
}

void init() {
    for (int i = 0; i < 100'005; i++) {
        adj[i].clear();
    }
    memset(parent, -1, sizeof(parent));
    fill(depth, depth+N, -1);
}

long long solve() {
    scanf("%d", &N);
    init();
    for (int i = 1; i < N; i++) {
        int v; scanf("%d", &v);
        v--;
        adj[v].push_back(i);
    }
    depth[0] = 0;

    queue<pair<int, int> > bq;
    bq.push({0,0});

    while(!bq.empty()) {
        auto c = bq.front(); bq.pop();
        int curr = c.first;
        int dept = c.second;
        
        for (int next: adj[curr]) {
            depth[next] = dept+1;
            parent[next][0] = curr;
            bq.push({next, dept+1});
        }
    }

    for (int j = 0; j < MAX-1; j++) {
        for (int i = 1; i < N; i++) {
            if (parent[i][j] != -1) {
                parent[i][j+1] = parent[ parent[i][j] ][j];
            }
        }
    }

    queue<int> q;
    q.push(0);
    int curr = 0;
    long long result = 0;

    while(!q.empty()) {
        int c = q.front(); q.pop();

        for (int next: adj[c]) {
            int w = lca(next, curr);
            int diff = depth[curr] + depth[next] - 2*depth[w];
            result += diff;
            curr = next;
            q.push(next);
        }
    }
    return result;
}

void testcase(int tc) {
    long long result = solve();
    printf("#%d %lld\n", tc, result);
}

int main() {
    freopen("../input.txt", "r", stdin);

    int T; scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}