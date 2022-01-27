#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>
//////
class node {
    public:
    int x, y, s;

    node():x(0),y(0),s(0){}
    node(int a, int b, int c): x(a), y(b), s(c) {}
};

class mingqueue {
    public:
    node arr[1003];
    int l = 0, r = 0;

    bool empty() { return l == r; }
    void push(node v) { arr[r++] = v; }
    node front() { return arr[l]; }
    void pop() { l++; }
};

int graph[11][11];
int m_size;
bool visit[11][11];

int di[4][2] = { {1,0}, {0,1}, {-1,0}, {0,-1}};

void bfs_init(int map_size, int map[10][10]) {
    m_size = map_size;
    for (int i = 1; i <= map_size; i++) {
        for (int j = 1; j <= map_size; j++) {
            graph[i][j] = map[i-1][j-1];
            visit[i][j] = false;
        }
    }
}

bool isPossible(int a, int b) {
    if (1 <= a && a <= m_size && 1<=b && b<= m_size) {
        if (!visit[b][a] && graph[b][a] == 0) { return true; }
    }
    return false;
}

int bfs(int x1, int y1, int x2, int y2) {
    for (int i = 1; i <= m_size; i++) {
        for (int j = 1; j <= m_size; j++) {
            visit[i][j] = false;
        }
    }

    mingqueue q;
    q.push(node(x1, y1, 0));
    visit[y1][x1] = true;

    int step = 0;
    while(!q.empty()) {
        node c = q.front(); q.pop();

        if (c.x == x2 && c.y == y2) { return c.s; }

        for (int i = 0; i < 4; i++) {
            int a = c.x + di[i][0];
            int b = c.y + di[i][1];
            if (isPossible(a, b)) { 
                visit[b][a] = true;
                q.push(node(a, b, c.s+1)); 
            }
        }
    }
    return -1;
}
///////

static int test_bfs() {
	int N;
	int map[10][10];
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			scanf("%d", &map[i][j]);
		}
	}
	bfs_init(N, map);
	int M;
	int score = 100;
	scanf("%d", &M);
	for (int i = 0; i < M; ++i) {
		int x1, y1, x2, y2;
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		int result = bfs(x1, y1, x2, y2);
		int dist;
		scanf("%d", &dist);
		if (result != dist) score = 0;
	}
	return score;
}

int main() {
	setbuf(stdout, NULL);
    freopen("../input.txt", "r", stdin);
	printf("#total score : %d\n", test_bfs());

	return 0;
}