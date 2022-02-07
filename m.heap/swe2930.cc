#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;
typedef long long ll;


class Heap {
    private:
    bool (*cmp) (int a, int b);
    void swap(int& a, int & b) {
        int t = b;
        b = a;
        a = t;
    }
    public:

    int h[100'005];
    int len = 0;

    Heap(bool (*cmpf) (int a, int b)) {
        cmp = cmpf;
        len = 0;
    }

    void push(int v) {
        h[++len] = v;
        int cur = len;
        while (cur != 1) {
            if ((*cmp)(h[cur], h[cur/2])) {
                swap(h[cur], h[cur/2]);
                cur /= 2;
            } else break;
        }
    }

    int pop() {
        if (len == 0) { return -1; }
        int ret = h[1];
        h[1] = h[len--];
        int cur = 1;
        while (cur * 2 <= len) {
            int chidx = cur * 2; // left
            if (chidx+1 <= len && (*cmp)(h[chidx+1], h[chidx])) {
                chidx++;
            }
            if ((*cmp)(h[chidx], h[cur])) {
                swap(h[chidx], h[cur]);
                cur = chidx;
            } else break;
        }
        return ret;
    }

    int top() {
        return h[1];
    }
};


bool max(int a, int b) {
    return a > b;
}

Heap heap(&max);

void solve() {
    int N; scanf ("%d", &N);
    priority_queue<int> pq;

    for (int i = 0; i < N; i++) {
        int op; scanf("%d", &op);
        if (op == 1) { int x; scanf("%d", &x); pq.push(x); }
        else {
            if (pq.empty()) { printf("-1 "); }
            else { printf("%d ", pq.top());  pq.pop(); } 
        }
    }
    
}

void testcase(int tc) {
    printf("#%d ", tc);
    solve();
    printf("\n");
}

int main() {
    freopen("../input.txt", "r", stdin);

    int T; scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}