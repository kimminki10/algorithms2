#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_NODE 10000

enum { ADD_HEAD = 1, ADD_TAIL, ADD_NUM, FIND, REMOVE, PRINT, PRINT_REVERSE, END = 99 };

//////////
#define MAX_NODE 10000

struct Node {
	int data;
	Node* prev;
	Node* next;
};

Node node[MAX_NODE];
int nodeCnt;
Node* head;
Node* tail;

Node* getNode(int data) {
	node[nodeCnt].data = data;
	node[nodeCnt].prev = nullptr;
	node[nodeCnt].next = nullptr;
	return &node[nodeCnt++];
}

void init()
{
    nodeCnt = 0;
    head = getNode(-1);
    tail = getNode(-1);
    head->next = tail;
    tail->prev = head;
}

void addNode2Head(int data) 
{
    Node* newNode = getNode(data);
    newNode->next = head->next;
    newNode->prev = head;

    head->next->prev = newNode;
    head->next = newNode;
}

void addNode2Tail(int data) 
{
    Node* newNode = getNode(data);
    newNode->next = tail;
    newNode->prev = tail->prev;

    tail->prev->next = newNode;
    tail->prev = newNode;
}

void addNode2Num(int data, int num) 
{
    Node* newNode = getNode(data);
    Node* n = head;
    
    for (int i = 0; i < num && n != tail; n = n->next, i++) {}

    newNode->next = n;
    newNode->prev = n->prev;

    n->prev->next = newNode;
    n->prev = newNode;
}

int findNode(int data) 
{
    int num = 0;
    for (Node* n = head; n != tail; n = n->next) {
        if (n->data == data) {
            break;
        }
        num++;
    }
    return num;
}

void removeNode(int data) 
{
    for (Node* n = head; n != tail; n = n->next) {
        if (n->data == data) {
            n->next->prev = n->prev;
            n->prev->next = n->next;
        }
    }
}

int getList(int output[MAX_NODE]) 
{
    int i = 0;
    for (Node* n = head->next; n != tail; n = n->next) {
        output[i++] = n->data;
    }
    return i;
}

int getReversedList(int output[MAX_NODE]) 
{
    int i = 0;
    for (Node* n = tail->prev; n != head; n = n->prev) {
        output[i++] = n->data;
    }
    return i;
}
//////////

static void run() {
	while (1) {
		int cmd, data, num, cnt, i = 0;
		int output[MAX_NODE] = { 0 };

		scanf("%d", &cmd);
		switch (cmd) {
		case ADD_HEAD: // 1
			scanf("%d", &data);
			addNode2Head(data);
			break;
		case ADD_TAIL: // 2
			scanf("%d", &data);
			addNode2Tail(data);
			break;
		case ADD_NUM: // 3
			scanf("%d %d", &data, &num);
			addNode2Num(data, num);
			break;
		case FIND: // 4
			scanf("%d", &data);
			num = findNode(data);
			printf("%d\n", num);
			break;
		case REMOVE: // 5
			scanf("%d", &data);
			removeNode(data);
			break;
		case PRINT: // 6
			cnt = getList(output);
			while (cnt--)
				printf("%d ", output[i++]);
			printf("\n");
			break;
		case PRINT_REVERSE: // 7
			cnt = getReversedList(output);
			while (cnt--)
				printf("%d ", output[i++]);
			printf("\n");
			break;
		case END:
			return;
		}
	}
}

int main(void) {
	//setbuf(stdout, NULL);
	//freopen("dll_input.txt", "r", stdin);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("#%d\n", t);
		init();
		run();
		printf("\n");
	}

	return 0;
}