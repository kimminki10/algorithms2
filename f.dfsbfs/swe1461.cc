#include <iostream>
#include <algorithm>

using namespace std;

int N;
int cell[12][12];
int core[12][2];
int coreNum=0;

int d[4][2] = {{0,1},{1,0},{-1,0},{0,-1}};

const int powered = 2;
const int unpowered = 1;
const int wire = 3;

int result = 987654321;
int maxCoreCount = 0;

bool isEdge(int x, int y) { return x == 0 || y == 0 || x == N-1 || y == N-1; }

int setWireAndGetNum(int x, int y, int i, int v) {
    int check = v==wire?0:wire;

    if (cell[x][y] == check) {
        if (isEdge(x,y)) { 
            cell[x][y] = v;
            return 1; 
        }
        else { 
            int r = setWireAndGetNum(x+d[i][0], y+d[i][1], i, v);
            if (r != -1) { cell[x][y] = v; return r+1; } 
        }
    }
    return -1;
}

void dfs(int cidx, int coreCount, int cost) {
    if (cidx >= coreNum) {
        if (coreCount > maxCoreCount) {
            maxCoreCount = coreCount;
            result = cost;
        } else if (coreCount == maxCoreCount && result > cost) { result = cost; }
        return;
    }

    int x = core[cidx][0];
    int y = core[cidx][1];

    if (isEdge(x,y) && cell[x][y] == powered) { 
        dfs(cidx+1, coreCount+1, cost); 
        return;
    }

    int flag = -1, c = -1;
    for (int i = 0; i < 4; i++) {
        cell[x][y] = powered;
        c = setWireAndGetNum(x+d[i][0], y+d[i][1], i, wire);

        flag = max(flag, c);
        if (c != -1) { dfs(cidx+1, coreCount+1, cost+c); }

        cell[x][y] = unpowered;
        setWireAndGetNum(x+d[i][0], y+d[i][1], i, 0);
    }
    if (flag == -1) { dfs(cidx+1, coreCount, cost); }
}

void solve() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> cell[i][j];
            if (cell[i][j] == unpowered) {
                core[coreNum  ][0] = i;
                core[coreNum++][1] = j;
                if (isEdge(i,j)) {cell[i][j]=powered;}
            }
        }
    }

    dfs(0, 0, 0);
}

void testcase(int tc) {
    result = 987654321;
    coreNum = 0;
    maxCoreCount = 0;

    solve();
    cout << "#" << tc << " " << result << "\n";
}

int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("../input.txt", "r", stdin);

    int T; cin>> T;
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}