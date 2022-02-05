#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int N, M;
int parent[100'000][18]; // u의 2**k 번째 부모
int depth[100'000];
vector<int> adj[100'001];

void dfs(int curr) {
    for (int next: adj[curr]) {
        if (depth[next] == -1) {
            parent[next][0] = curr;
            depth[next] = depth[curr] +  1;
            dfs(next);
        }
    }
}

void solve() {
    scanf("%d", &N);
    for (int i = 0; i < N-1; i++) {
        int a, b; scanf("%d %d", &a, &b);
        a--, b--;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    memset(parent, -1, sizeof(parent));
    fill(depth, depth+N, -1);
    depth[0] = 0;

    dfs(0);

    for (int j=0; j<17; j++) {
        for (int i = 1; i<N; i++) {
            if (parent[i][j] != -1) {
                parent[i][j+1] = parent[ parent[i][j] ][j];
            }
        }
    }
    

    scanf("%d", &M);
    for (int i=0; i<M; i++) {
        int a,b; scanf("%d %d", &a, &b);
        a--,b--;

        if (depth[a] < depth[b]) swap(a, b);
        int diff = depth[a] - depth[b];

        for (int j=0; diff; j++) {
            if (diff%2) a = parent[a][j];
            diff /= 2;
        }

        if (a != b) {
            for (int j=17; j>=0; j--) {
                if (parent[a][j] != -1 && parent[a][j] != parent[b][j]) {
                    a = parent[a][j];
                    b = parent[b][j];
                }
            }
            a = parent[a][0];
        }
        printf("%d\n", a+1);
    }
}

int main() {
    freopen("../input.txt", "r", stdin);
    solve();
}