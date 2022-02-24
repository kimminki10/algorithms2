#include <cstdio>

int mapmap[20][20];
int graph[20][20];
const int GARO=0;
const int SERO=1;
const int LETE=2;
int N;

bool isGood(int x, int y, int T) {
    if (!(0<=x && x < N && 0<=y && y<N)) { return false; }
    if (mapmap[x][y] == 1) { return false; }

    if (T == LETE) {
        if (mapmap[x-1][y]==1) { return false; }
        if (mapmap[x][y-1]==1) { return false; }
    }

    return true;
}

void dfs(int x, int y, int T) {
    if (isGood(x+1,y+1, LETE)) {graph[x+1][y+1]+=1; dfs(x+1, y+1, LETE); }

    if      (T == GARO && isGood(x,y+1, GARO)) { graph[x][y+1]+=1; dfs(x, y+1, GARO); }
    else if (T == SERO && isGood(x+1,y, SERO)) { graph[x+1][y]+=1; dfs(x+1, y, SERO); }
    else if (T == LETE) {
        if (isGood(x,y+1, GARO)) { graph[x][y+1]+=1; dfs(x, y+1, GARO);}
        if (isGood(x+1,y, SERO)) { graph[x+1][y]+=1; dfs(x+1, y, SERO); }
    }
}

int main() {
    scanf("%d", &N);

    for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) {
        scanf("%d", &mapmap[i][j]);
    }

    graph[0][1] = 1;
    dfs(0,1,GARO);
    printf("%d\n", graph[N-1][N-1]);
}