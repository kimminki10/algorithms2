#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;
typedef long long ll;

struct node {
    int x,y;
    node(): node(-1,-1) {}
    node(int a, int b): x(a), y(b){}
    bool operator < (const node & n) const {return x < n.x;}
};

const int INF = 987654321;
int g[100][100];
int dist[100][100];
int d[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};
int N; 

inline bool isgood(int x, int y) { return 0 <= x && x < N && 0 <= y && y < N; }
void dijkstra(int sx, int sy) {
    for (int i = 0; i < 100; i++) {
        for (int j = 0 ; j < 100; j++) {
            dist[i][j] = INF;
        }
    }
    dist[sx][sy] = 0;

    priority_queue< pair<int, node> > pq;
    pq.push({0, {sx, sy}});

    while(!pq.empty()) {
        int cost = -pq.top().first;
        node v = pq.top().second;
        pq.pop();

        if (dist[v.x][v.y] < cost) { continue; }

        for (int i = 0; i < 4; i++) {
            int x = v.x + d[i][0];
            int y = v.y + d[i][1];
            if (!isgood(x, y)) { continue; }

            int nd = cost + g[x][y];
            if (dist[x][y] > nd) {
                dist[x][y] = nd;
                pq.push({-nd, {x, y}});
            }
        }
    }
}

int solve() {
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int v; scanf("%1d", &v);
            g[i][j] = v;
        }
    }

    dijkstra(0, 0);
    return dist[N-1][N-1];
}

void testcase(int tc) {
    int result = solve();
    printf("#%d %d\n", tc, result);
}

int main() {
    freopen("../input.txt", "r", stdin);

    int T; scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}