#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;
typedef long long ll;

ll solve() {
    priority_queue<int, vector<int>, less<int> > aq; // max
    priority_queue<int, vector<int>, greater<int> > bq; // min

    int N, A; scanf("%d %d", &N, &A);
    ll result = 0;
    aq.push(A);
    for (int i = 0; i < N; i++) {
        int x, y; scanf("%d %d", &x, &y);
        aq.push(x);
        aq.push(y);

        while (!bq.empty()) { aq.push(bq.top()); bq.pop(); }

        while (bq.size()+1 != aq.size()) {
            bq.push(aq.top()); aq.pop();
        }
        result = (result+aq.top()) % 20171109;
    }
    return result;
}

void testcase(int tc) {
    ll result = solve();
    printf("#%d %lld\n", tc, result);
}

int main() {
    freopen("../input.txt", "r", stdin);

    int T; scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}