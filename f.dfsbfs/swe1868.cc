#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int N;
vector<string> table;
int check[300][300];
bool visit[300][300];
int bombNum = 0;
vector<pair<int, int> > zeros;

inline bool isPossible(int x, int y) { return 0 <= x && x < N && 0 <= y && y < N; }

int eval(int x, int y) {
    if (table[x][y] == '*') { return -1; }

    int result = 0;
    for (int i = x-1; i <= x+1; i++) {
        for (int j = y-1; j <= y+1; j++) {
            if (isPossible(i,j)) {
                if (table[i][j] == '*') {
                    result += 1;
                }
            }
        }
    }
    return result;
}

int bfs(int x, int y) {
    queue<pair<int, int> > q;
    q.push({x, y});
    visit[x][y] = true;
    int result = 1;

    while(!q.empty()) {
        auto c = q.front(); q.pop();

        int i = c.first;
        int j = c.second;

        if (check[i][j] != 0) { continue; }

        for (int a = i-1; a<=i+1; a++) {
            for (int b = j-1; b<=j+1; b++) {
                if (isPossible(a, b) && visit[a][b] == false && check[a][b] != -1) { 
                    visit[a][b] = true; 
                    q.push({a, b}); 
                    result++; 
                }
            }
        }
    }
    return result;
}

int solve() {
    int result = 0;
    cin >> N;
    for (int i = 0; i < N; i++) {
        string r; cin >> r;
        table.push_back(r);
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            check[i][j] = eval(i,j);
            if (table[i][j] == '*') { bombNum += 1; }
            else if (check[i][j] == 0) {
                zeros.push_back({i, j});
            }
        }
    }

    int zeroisland = 0;
    int count = 0;
    for (int i = 0; i < (int)zeros.size(); i++) {
        int x = zeros[i].first;
        int y = zeros[i].second;

        if (visit[x][y] == true) { continue; }
        count += 1;
        zeroisland += bfs(x, y);
    }
    result = N*N - bombNum - zeroisland + count;
    return result;
}

void testcase(int tc) {
    bombNum = 0;
    zeros.clear();
    table.clear();
    for (int i = 0; i < 300; i++) {
        for (int j = 0; j < 300; j++) {
            check[i][j] = -1;
            visit[i][j] = false;
        }
    }
    int result = solve();
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