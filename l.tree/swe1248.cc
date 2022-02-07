#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;
const int MAX = 17;

int parent[10'000][MAX];
int depth[10'000];
int subNum[10'000];
vector<int> adj[10'000];

int V, E;

int dfs(int curr) {
    for (int next: adj[curr]) {
        if (depth[next] == -1) {
            parent[next][0] = curr;
            depth[next] = depth[curr] + 1;

            subNum[curr] += dfs(next);
        }
    }
    return subNum[curr];
}

int lca(int x, int y) {
    if (depth[x] < depth[y]) { swap(x, y); }
    int diff = depth[x] - depth[y];

    for (int i = 0; diff; i++) {
        if (diff%2) x = parent[x][i];
        diff /= 2;
    }

    if (x!=y) {
        for (int i = MAX-1; i >= 0; i--) {
            if (parent[x][i] != -1 && parent[x][i] != parent[y][i]) {
                x = parent[x][i];
                y = parent[y][i];
            }
        }
        x = parent[x][0];
    }
    return x;
}

void init() {
    memset(parent, -1, sizeof(parent));
    fill(depth, depth+V, -1);
    fill(subNum, subNum+V, 1);
    for (int i = 0; i < V; i++) {
        adj[i].clear();
    }
}
void testcase(int tc) {
    int x, y;
    scanf("%d %d %d %d", &V, &E, &x, &y);
    init();

    for (int i = 0; i < E; i++) {
        int p, c; scanf(" %d %d", &p, &c);
        p--,c--;
        adj[p].push_back(c);
    }

    depth[0] = 0;
    dfs(0);

    for (int j = 0; j < MAX; j++) {
        for (int i = 1; i < V; i++) {
            if (parent[i][j] != -1) {
                parent[i][j+1] = parent[ parent[i][j] ][j];
            }
        }
    }

    int w = lca(x-1, y-1);

    printf("#%d %d %d\n", tc, w+1, subNum[w]);
}

int main() {
    freopen("../input.txt", "r", stdin);

    int T; scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}