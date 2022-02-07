#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

#define CMD_MKDIR 1
#define CMD_RM 2
#define CMD_CP 3
#define CMD_MV 4
#define CMD_FIND 5

#define NAME_MAXLEN 6
#define PATH_MAXLEN 1999
////////
struct Node;

struct LinkedNode {
    Node* n = nullptr;
    LinkedNode* next = nullptr;
};

LinkedNode linknodes[150'000];
int linknodeCnt = 0;

LinkedNode* getLinkNode() { 
    linknodes[linknodeCnt].n = nullptr;
    linknodes[linknodeCnt].next = nullptr;
    return &linknodes[linknodeCnt++]; 
}

struct Node {
    int name = 0;
    Node* parent = nullptr;
    int count = 1;
    LinkedNode* child = nullptr;
};

Node nodes[50'000];
int nodeCnt = 0;
Node* root;

Node* getNode() { 
    nodes[nodeCnt].child = nullptr;
    nodes[nodeCnt].parent = nullptr;
    nodes[nodeCnt].count = 1;
    nodes[nodeCnt].name = 0;

    return &nodes[nodeCnt++]; 
}

int intName(char* name) {
    int result = 0;
    for (int i = 0; name[i] != '\0' && name[i] != '/'; ++i) {
        result <<= 5;
        result += (int)(name[i] - 'a' + 1);
    }
    return result;
}

Node* findNode(char path[PATH_MAXLEN + 1]) {
    Node* cur = root;
    for (int i = 0; path[i + 1] != '\0'; i++) {
        if (path[i] == '/') {
            int iname = intName(path + i + 1);
            for (LinkedNode* ln = cur->child; ln != nullptr; ln = ln->next) {
                if (ln->n->name == iname) {
                    cur = ln->n;
                    break;
                }
            }
        }
    }
    return cur;
}

void init(int n) {
    linknodeCnt = 0;
    nodeCnt = 0;
    
    root = getNode();
}

void cmd_mkdir(char path[PATH_MAXLEN + 1], char name[NAME_MAXLEN + 1]) {
    Node* cur = findNode(path);

    Node* newNode = getNode();
    newNode->name = intName(name);
    newNode->parent = cur;

    LinkedNode* newLink = getLinkNode();
    newLink->n = newNode;

    newLink->next = cur->child;
    cur->child = newLink;

    for (Node* n = newNode->parent; n != nullptr; n = n->parent) {
        n->count += newNode->count;
    }
}

void cmd_rm(char path[PATH_MAXLEN + 1]) {
    Node* cur = findNode(path);
    for (Node* n = cur->parent; n != nullptr; n = n->parent) {
        n->count -= cur->count;
    }

    Node* pa = cur->parent;
    if (pa->child->n->name == cur->name) {
        pa->child = pa->child->next;
    } else {
        for (LinkedNode* ln = pa->child; ln->next != nullptr; ln = ln->next) {
            if (ln->next->n->name == cur->name) {
                ln->next = ln->next->next;
                break;
            }
        }
    }
}

void cpNode(Node* src, Node* dst) {
    dst->name = src->name;
    dst->count = src->count;
    for (LinkedNode* ln = src->child; ln != nullptr; ln = ln->next) {
        LinkedNode* newLink = getLinkNode();
        Node* newNode = getNode();
        newLink->n = newNode;
        newNode->parent = dst;

        if (dst->child != nullptr) {
            newLink->next = dst->child;
        }
        dst->child = newLink;

        cpNode(ln->n, newNode);
    }
}

void cmd_cp(char srcPath[PATH_MAXLEN + 1], char dstPath[PATH_MAXLEN + 1]) {
    Node* srcCur = findNode(srcPath);
    Node* dstCur = findNode(dstPath);

    Node* newNode = getNode();
    cpNode(srcCur, newNode);
    newNode->parent = dstCur;

    LinkedNode* newLink = getLinkNode();
    newLink->n = newNode;

    newLink->next = dstCur->child;
    dstCur->child = newLink;

    for (Node* n = newNode->parent; n != nullptr; n = n->parent) {
        n->count += newNode->count;
    }
}

void cmd_mv(char srcPath[PATH_MAXLEN + 1], char dstPath[PATH_MAXLEN + 1]) {
    Node* srcCur = findNode(srcPath);
    Node* dstCur = findNode(dstPath);

    for (Node* n = srcCur->parent; n != nullptr; n = n->parent) {
        n->count -= srcCur->count;
    }
    Node* pa = srcCur->parent;
    if (pa->child->n->name == srcCur->name) {
        pa->child = pa->child->next;
    } else {
        for (LinkedNode* ln = pa->child; ln->next != nullptr; ln = ln->next) {
            if (ln->next->n->name == srcCur->name) {
                ln->next = ln->next->next;
                break;
            }
        }
    }

    LinkedNode* newLink = getLinkNode();
    newLink->n = srcCur;

    if (dstCur->child != nullptr) {
        newLink->next = dstCur->child;
    }
    dstCur->child = newLink;
    srcCur->parent = dstCur;

    for (Node* n = srcCur->parent; n != nullptr; n = n->parent) {
        n->count += srcCur->count;
    }
}

int cmd_find(char path[PATH_MAXLEN + 1]) {
    Node* cur = findNode(path);
    return cur->count - 1;
}
////////
static bool run(int m) {
    bool isAccepted = true;
    int cmd;
    char name[NAME_MAXLEN + 1];
    char path1[PATH_MAXLEN + 1], path2[PATH_MAXLEN + 1];

    while (m--) {
        scanf("%d", &cmd);

        if (cmd == CMD_MKDIR) {
            scanf("%s%s", path1, name);
            cmd_mkdir(path1, name);
        } else if (cmd == CMD_RM) {
            scanf("%s", path1);
            cmd_rm(path1);
        } else if (cmd == CMD_CP) {
            scanf("%s%s", path1, path2);
            cmd_cp(path1, path2);
        } else if (cmd == CMD_MV) {
            scanf("%s%s", path1, path2);
            cmd_mv(path1, path2);
        } else {
            int ret;
            int answer;

            scanf("%s", path1);
            ret = cmd_find(path1);
            scanf("%d", &answer);

            isAccepted &= (ret == answer);
        }
    }

    return isAccepted;
}

int main(void) {
    int test, T;
    int n, m;

    freopen("../input.txt", "r", stdin);

    setbuf(stdout, NULL);

    scanf("%d", &T);

    for (test = 1; test <= T; ++test) {
        scanf("%d%d", &n, &m);

        init(n);

        if (run(m)) {
            printf("#%d 100\n", test);
        } else {
            printf("#%d 0\n", test);
        }
    }

    return 0;
}