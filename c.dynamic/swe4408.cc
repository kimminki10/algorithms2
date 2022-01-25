#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve() {
    int result = 0;
    int N;
    vector<pair<int, int> > move;

    cin >> N;
    for (int i = 0; i < N; i++) {
        int from, to; cin >> from >> to;
        if (from % 2) from += 1;
        if (to % 2)   to += 1;
        if (to < from) {
            int tmp = to;
            to = from;
            from = tmp;
        }
        move.push_back({from, to});
    }

    sort(move.begin(), move.end());

    vector<int> doneIdx;
    int r = 0;
    vector<pair<int, int> > todo(move);
    while (!todo.empty()) {
        int size = (int)todo.size();

        for (int i = 0; i < size; i++) {
            auto c = todo[i];
            if (r < c.first) {
                r = c.second;
                doneIdx.push_back(i);
            }
        }
        
        for (int i = (int)doneIdx.size()-1; i >= 0 ; i--) {
            todo.erase(todo.begin() + doneIdx[i]);
        }
        doneIdx.clear();
        result += 1;
        r = 0;
    }
    
    return result;
}

void testcase(int tc) {
    int result = 0;

    result = solve();
    cout << "#" << tc <<  " " << result << endl;
}

int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("input.txt", "r", stdin);
    int T; cin >> T;
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }    
}