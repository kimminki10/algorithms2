#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


enum { ADD_HEAD = 1, ADD_TAIL, ADD_NUM, REMOVE, PRINT, END = 99 };


//////////////////////////////////////////////////////

#define MAX_NODE 10000

struct Node {
	int data;
	Node* next;
};

Node node[MAX_NODE];
int nodeCnt;
Node* head;

Node* getNode(int data) {
	node[nodeCnt].data = data;
	node[nodeCnt].next = nullptr;
	return &node[nodeCnt++];
}

void init()
{
    nodeCnt = 0;
    head = getNode(-1);
}

void addNode2Head(int data) 
{
    Node* newNode = getNode(data);
    newNode->next = head->next;
    head->next = newNode;
}

void addNode2Tail(int data) 
{
    Node* cur = head;
    while(cur->next) {cur = cur->next;}

    Node* newNode = getNode(data);
    cur->next = newNode;
}

void addNode2Num(int data, int num) 
{
    Node* cur = head;
    for (int i = 1; i < num; i++) {
        cur = cur->next;
    }
    
    Node* newNode = getNode(data);
    newNode->next = cur->next;
    cur->next = newNode;
}

void removeNode(int data) 
{
    Node* cur = head;
    while(cur->next) { 
        if (cur->next->data == data) {
            cur->next = cur->next->next;
            break;
        }
        cur = cur->next; 
    }
}

int getList(int output[MAX_NODE]) 
{
    Node* cur = head->next;
    int i = 0;
    while(cur) {
        output[i++] = cur->data;
        cur = cur->next;
    }
    return i;
}
//////////////////////////////////////////////////////

static void run() {
	while (1) {
		int cmd, data, num, cnt, i;
		int output[MAX_NODE] = { 0 };

		scanf("%d", &cmd);
		switch (cmd) {
		case ADD_HEAD:
			scanf("%d", &data);
			addNode2Head(data);
			break;
		case ADD_TAIL:
			scanf("%d", &data);
			addNode2Tail(data);
			break;
		case ADD_NUM:
			scanf("%d %d", &data, &num);
			addNode2Num(data, num);
			break;
		case REMOVE:
			scanf("%d", &data);
			removeNode(data);
			break;
		case PRINT:
			cnt = getList(output);
			i = 0;
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
	setbuf(stdout, NULL);
	freopen("input.txt", "r", stdin);

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