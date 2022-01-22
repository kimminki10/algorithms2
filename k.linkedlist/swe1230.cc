#include <iostream>

using namespace std;
const int MAX_NODE = 100000;
struct Node {
    int data;
    Node* next;
    Node* prev;
};

int nodeCnt = 0;
Node node[MAX_NODE];
Node* head;
Node* tail;

Node* getNode(int data) {
	node[nodeCnt].data = data;
	node[nodeCnt].prev = nullptr;
	node[nodeCnt].next = nullptr;
	return &node[nodeCnt++];
}

void init() {
    nodeCnt = 0;
    head = getNode(-1);
    tail = getNode(-1);
    head->next = tail;
    tail->prev = head;
}

void append(int data) 
{
    Node* newNode = getNode(data);
    newNode->next = tail;
    newNode->prev = tail->prev;

    tail->prev->next = newNode;
    tail->prev = newNode;
}

void opInsert() {
    int x, y;
    int s;
    cin >> x >> y;

    Node* n = head;
    for (int i = 0; i <= x && n != tail; n = n->next, i++) {}

    for (int i = 0; i < y; i++) {
        cin >> s;
        Node* newNode = getNode(s);
        newNode->next = n;
        newNode->prev = n->prev;

        n->prev->next = newNode;
        n->prev = newNode;
    }
}

void opDelete() {
    int x, y;
    cin >> x >> y;

    Node* n = head;
    for (int i = 0; i <= x && n != tail; n = n->next, i++) {}

    for (int i = 0; i < y; i++, n = n->next) {
        n->next->prev = n->prev;
        n->prev->next = n->next;
    }
}

void opAppend() {
    int y, s;
    cin >> y;

    for (int i = 0; i < y; i++) {
        cin >> s;
        Node* newNode = getNode(s);
        newNode->next = tail;
        newNode->prev = tail->prev;

        tail->prev->next = newNode;
        tail->prev = newNode;
    }
}

void getList(int output[MAX_NODE]) 
{
    int i = 0;
    for (Node* n = head->next; i < 10 && n != tail; n = n->next) {
        output[i++] = n->data;
    }
}

void testcase(int tc) {
    init();
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        int v; cin >> v;
        append(v);
    }

    cin >> N;
    for (int i = 0; i < N; i++) {
        string op; cin >> op;
        if (op.compare("I") == 0) {
            opInsert();
        } else if (op.compare("D") == 0) {
            opDelete();
        } else if (op.compare("A") == 0) {
            opAppend();
        }
    }

    int output[MAX_NODE];
    getList(output);

    cout << "#" << (tc+1) << " ";

    for (int i = 0; i < 10; i++) {
        cout << output[i] << " ";
    }
    cout << endl;
}

int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);

    freopen("input.txt", "r", stdin);
    for (int i = 0; i < 10; i++) {
        testcase(i);
    }
}