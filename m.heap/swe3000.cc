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
        int x[2]; scanf("%d %d", &x[0], &x[1]);
        
        for (int j = 0; j < 2; j++) {
            int v = x[j];
            if (aq.size() == bq.size()) {
                if (bq.top() < v) {
                    aq.push(bq.top()); bq.pop();
                    bq.push(v);
                } else {
                    aq.push(v);
                }
            }
            else if (aq.top() > v) {
                bq.push(aq.top()); aq.pop();
                aq.push(v);
            } else {
                bq.push(v);
            }
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