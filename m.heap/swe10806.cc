#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long ll;

int N, X=0, D=1, K;
int A[10];

struct node {
    int cnt = 0;
    int k = 0;
    bool operator < (const node &n) const {
        return cnt < n.cnt;
    }
};

struct heap {
    node h[100'000];
    int len=0;

    void push(node v) {
        h[++len] = v;
        int cur = len;
        while (cur != 1) {
            if (h[cur] < h[cur/2]) {
                swap(h[cur], h[cur/2]);
                cur /= 2;
            } else break;
        }
    }

    node pop() {
        node ret = h[1];
        h[1] = h[len--];
        int cur = 1;
        while (cur * 2 <= len) {
            int chidx = cur * 2;
            if (chidx + 1 <= len && h[chidx+1] < h[chidx]) {
                chidx++;
            }

            if (h[chidx] < h[cur]) {
                swap(h[chidx], h[cur]);
                cur = chidx;
            } else { break; }
        }
        return ret;
    }

    bool isEmpty() { return len == 0; }
};

int solve() {
    scanf("%d", &N); X=0; D=1;
    for (int i = 0; i < N; i++) { 
        scanf("%d", &A[i]);
    }
    scanf("%d", &K);

    heap pq;
    pq.push({0, K});
    while(!pq.isEmpty()) {
        node c = pq.pop();

        if (c.k == 0) break;
        pq.push({c.cnt+c.k, 0});
        for (int i = 0; i < N; i++) {
            pq.push({c.cnt + c.k%A[i], c.k/A[i]});
        }
    }
    return pq.pop().cnt;
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