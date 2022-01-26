#include <iostream>
#include <set>
#include <string>

using namespace std;

int N;

struct cmp {
    bool operator() (const string& a, const string& b) {
        if (a.length() != b.length()) {
            return a.length() < b.length();
        }
        return a.compare(b) < 0;
    }
};

set<string, cmp> nameSet;

void solve() {
    cin>> N;
    for (int i = 0; i < N; i++) {
        string tmp; cin >> tmp;
        nameSet.insert(tmp);
    }

    for (auto s : nameSet ) {
        cout << s << "\n";
    }
}

void testcase(int tc) {
    nameSet .clear();
    cout << "#" << tc << "\n";
    solve();
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