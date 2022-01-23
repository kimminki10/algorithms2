#include <iostream>

using namespace std;

const int MAX_SIZE = 10000;
class Node {
    public:
    int data;
    Node* next = nullptr;
    Node* prev = nullptr;
};

Node node[MAX_SIZE];
int nodeCnt = 0;
Node* head;
Node* tail;

Node* getNode(int data) {
    node[nodeCnt].data = data;
    return &node[nodeCnt++];
}

void init() {
    nodeCnt = 0;
    head = getNode(-1);
    tail = getNode(-1);
    head->next = tail;
    tail->prev = head;
}

void put(int data, int num) {
    Node* n = head;
    for (int i = 0; i <= num && n != tail; n = n->next, i++) {}

    Node* newNode = getNode(data);
    newNode->next = n;
    newNode->prev = n->prev;

    n->prev->next = newNode;
    n->prev = newNode;
}

void remove(int num) {
    Node* n = head;
    for (int i = 0; i <= num && n != tail; n = n->next, i++) {}

    n->prev->next = n->next;
    n->next->prev = n->prev;
}

void setData(int data, int num) {
    Node* n = head;
    for (int i = 0; i <= num && n != tail; n = n->next, i++) {}

    n->data=  data;
}

void append(int data) {
    Node* newNode = getNode(data);

    newNode->next = tail;
    newNode->prev = tail->prev;

    tail->prev->next = newNode;
    tail->prev = newNode;
}

void testcase(int tc) {
    init();
    int n, m, l;
    cin >> n >> m >> l;
    int result = 0;

    for (int i = 0; i < n; i++) {
        int s; cin >> s;
        append(s);
    }

    for (int i = 0; i < m; i++) {
        string op; cin >> op;
        if (op.compare("I") == 0) {
            int a, b; cin >> a >> b;
            put(b, a);
        } else if (op.compare("D") == 0) {
            int a; cin >> a;
            remove(a);
        } else {
            int a, b; cin >> a >> b;
            setData(b, a);
        }
    }

    result = -1;
    Node* no = head->next;
    for (int i = 0; no != tail; i++, no = no->next) {
        if (i == l) {
            result = no->data;
            break;
        }
    }

    printf("#%d %d\n", tc, result);
}

int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);
    //freopen("input.txt", "r", stdin);

    int T; cin>>T;
    for(int i = 0; i < T; i++) {
        testcase(i+1);
    }
}