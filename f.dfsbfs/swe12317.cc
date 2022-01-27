#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

static unsigned int seed = 12345;
static unsigned int pseudo_rand(int max) {
	seed = ((unsigned long long)seed * 1103515245 + 12345) & 0x7FFFFFFF;
	return seed % max;
}

#define MAX_N (40)
#define MAX_K (98)
#define MIN_N (2)
#define MAX_CHILD (5)


//////
class mingvec {
    public:
    int arr[101] = {0,};
    int idx = 0;

    void clear() { idx = 0; }
    void push_back(int v) { arr[idx++] = v; }

	int at(int i) { return arr[i]; }
	int size() { return idx; }
};

class mingstack {
    public:
    int arr[1003]={0,};
    int idx = 0;

    bool empty() { return idx == 0; }
    void push(int v) { arr[idx++] = v; }
    int top() { return arr[idx-1]; }
    void pop() { idx--; }
};

mingvec graph[101];
void dfs_init(int N, int path[100][2])
{
    for (int i = 0; i < 101; i++) {
        graph[i].clear();
    }

    for (int i = N-1; i >= 0; i--) {
        graph[path[i][0]].push_back(path[i][1]);
    }
}

int dfs(int n)
{
    bool visit[101] = {false,};
    mingstack s;
    s.push(n);

    while(!s.empty()) {
        int c = s.top(); s.pop();

        visit[c] = true;
        if (c > n) { return c; }
		
        for (int i = 0; i < graph[c].size(); i++) {
			int v = graph[c].at(i);

            if (!visit[v]) {
                s.push(v);
            }
        }
    }
	return -1;
}

//////

static int p[MAX_K+2];
static int c[MAX_K+2];
static int path[MAX_N][2];
static void makeTree(int n) {
	for (int i = 1; i < MAX_K+2; ++i) {
		p[i] = c[i] = -1;
	}
	c[pseudo_rand(MAX_K + 1) + 1] = 0;
	for (int i = 0; i < n; ++i) {
		int pi = pseudo_rand(MAX_K + 1) + 1;
		while (c[pi] < 0 || c[pi] >= MAX_CHILD) {
			++pi;
			if (pi == MAX_K + 2)
				pi = 1;
		}
		int ci = pseudo_rand(MAX_K + 1) + 1;
		while (c[ci] >= 0) {
			++ci;
			if (ci == MAX_K + 2)
				ci = 1;
		}
		p[ci] = pi;
		++c[pi];
		c[ci] = 0;
	}
	bool check[MAX_K + 2] = { false };
	for (int i = 0; i < n; ++i) {
		int e = pseudo_rand(MAX_K + 1) + 1;
		while (check[e] || c[e] < 0 || p[e] == -1) {
			++e;
			if (e == MAX_K + 2)
				e = 1;
		}
		check[e] = true;
		path[i][0] = p[e];
		path[i][1] = e;
	}
}

int main() {
	setbuf(stdout, NULL);
	int T;
	freopen("../input.txt", "r", stdin);
	scanf("%d", &T);

	int totalScore = 0;
	for (int tc = 1; tc <= T; tc++) {
		int n, q;

		scanf("%d %d %d", &n, &q, &seed);

		makeTree(n - 1);
		dfs_init(n, path);

		bool check[MAX_K + 2] = { false };
		int score = 100;
		for (int i = 0; i < q; ++i) {
			int k, ret, correct;

			scanf("%d", &k);

			ret = dfs(k);

			scanf("%d", &correct);

			if (ret != correct)
				score = 0;
		}
		printf("#%d : %d\n", tc, score);
		totalScore += score;
	}
	printf("#total score : %d\n", totalScore / T);

	return 0;
}