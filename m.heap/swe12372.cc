#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_INPUT 10000
#define MAX_NUM 30000

///////
struct Node {
    int uid = -1;
    int income = -1;
    Node(): Node(-1, -1) {}
    Node(int u, int i): uid(u), income(i) {}

    bool operator < (const Node & n) const { 
        if (income > n.income) {
            return true;
        } else if (income == n.income) {
            return uid < n.uid;
        } else {
            return false;
        }
    }
};

class Heap {
    private:
    bool (*cmp) (Node a, Node b);
    void swap(Node& a, Node & b) {
        Node t = b;
        b = a;
        a = t;
    }
    public:

    Node h[100'005];
    int len = 0;

    Heap(bool (*cmpf) (Node a, Node b)) {
        cmp = cmpf;
        len = 0;
    }

    void push(Node v) {
        h[++len] = v;
        int cur = len;
        while (cur != 1) {
            if ((*cmp)(h[cur], h[cur/2])) {
                swap(h[cur], h[cur/2]);
                cur /= 2;
            } else break;
        }
    }

    Node pop() {
        Node ret = h[1];
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
        return h[1].uid;
    }
};

bool min(Node a, Node b) {
    return a < b;
}

Heap heap(&min);

void init() {
    heap.len = 0;
}

void addUser(int uID, int income) {
    heap.push(Node(uID, income));
}

int getTop10(int result[10]) {
    int ret = heap.len > 10? 10: heap.len;
    Node temp[10];
    for (int i = 0; i < ret; i++) {
        temp[i] = heap.pop();
        result[i] = temp[i].uid;
    }
    for (int i = 0; i < ret; i++) {
        heap.push(temp[i]);
    }
    return ret;
}
///////

static int input[MAX_INPUT];

static unsigned int seed = 13410;

static unsigned int pseudoRand() {
    seed = seed * 214013 + 2531011;
    return (unsigned int)(seed >> 11) % MAX_NUM;
}

static void makeInput(int inputLen) {
    for (int i = 0; i < inputLen; i++) {
        input[i] = pseudoRand();
    }
}

static int run() {
    int N, userNum, uID = 0;
    int score = 100, result[10], cnt;
    int sum, check;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &userNum);
        makeInput(userNum);
        for (int j = 0; j < userNum; j++) {
            addUser(uID++, input[j]);
        }
        cnt = getTop10(result);

        sum = 0;
        for (int j = 0; j < cnt; j++) sum += result[j];
        scanf("%d", &check);
        if (check != sum) {
            score = 0;
        }
    }
    return score;
}

int main(void) {
    setbuf(stdout, NULL);
    freopen("../input.txt", "r", stdin);
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {
        init();
        printf("#%d %d\n", tc, run());
    }
    return 0;
}