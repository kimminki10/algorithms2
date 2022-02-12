#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

#define CMD_INIT       100
#define CMD_INSERT     200
#define CMD_MOVECURSOR 300
#define CMD_COUNT      400
///////////////
#include <cstring>
inline int charToNum(char c) { return c - 'a' + 1; }
struct Node {
    char c = '\0';
    Node *n = nullptr;
    Node *p = nullptr;
} nodes[900'001];
int nodeCnt = 0;

void addNode(Node *cur, char c) {
    Node *nn = &nodes[nodeCnt++];
	nn->c = c;

	nn->n = cur->n;
	nn->p = cur;
	cur->n->p = nn; 
	cur->n = nn;
}

int H, W;
Node *head = new Node();
Node *tail = new Node();

Node *cur;
int nrow, ncol;

int rowCharNum[302][27];
int cntRow[302];
int minCnt[27];
int charNum = 0;

Node *rowStart[302];
void init(int h, int w, char mStr[]) {
	memset(rowCharNum, 0, sizeof(rowCharNum));
	memset(cntRow, 0, sizeof(cntRow));
	memset(minCnt, 0, sizeof(minCnt));

    H = h, W = w;

	head->n = tail;
	tail->p = head;
	tail->c = '$';

	cur = head;
	nrow=1, ncol=1;

	rowStart[1] = head;

	charNum = 0;

	int mStrLen = strlen(mStr);
	for (int i = 1; i <= mStrLen; i++) {
		int row = (i-1)/W + 1;
		addNode(cur, mStr[i-1]);
		cur=cur->n;
		charNum += 1;
		cntRow[row]++;
		if (i % W == 0) { rowStart[row+1] = cur; }

		rowCharNum[row][charToNum(mStr[i-1])]++;
	}
	cur = head;
	ncol = 1; nrow = 1;
}

void insert(char mChar) {
    addNode(cur, mChar); charNum += 1;
	rowCharNum[nrow][charToNum(mChar)]++; cntRow[nrow]++;
	minCnt[charToNum(mChar)]++;
	
	for (int r = nrow; r <= H; r++) {
		if (cntRow[r] <= W) {
			if (cntRow[r] == W) { rowStart[r+1] = tail->p; }
			break;
		}

		rowCharNum[r  ][charToNum(rowStart[r+1]->c)]--; cntRow[r  ]--;
		rowCharNum[r+1][charToNum(rowStart[r+1]->c)]++; cntRow[r+1]++;
		rowStart[r+1] = rowStart[r+1]->p;
	}

	if (ncol + 1 > W) { ncol = 1; nrow += 1; memset(minCnt, 0, sizeof(minCnt)); } 
	else { ncol += 1; }
	cur = cur->n;
}

char moveCursor(int mRow, int mCol) {
	memset(minCnt, 0, sizeof(minCnt)); 

	int t = (mRow-1) * W + mCol;
	if (t > charNum) { // 맨끝으로 이동
		nrow = charNum/W + 1; 
		ncol = charNum%W + 1;
	} else {
		nrow = mRow; ncol = mCol;
	}

	cur = rowStart[nrow];
	for (int i = 0; i < ncol-1; i++) { 
		minCnt[charToNum(cur->n->c)]++;
		cur = cur->n; 
	}
	return cur->n->c;
}

int countCharacter(char mChar) {
	int ret = 0;
	for (int r = nrow; cntRow[r] != 0; r++) {
		ret += rowCharNum[r][charToNum(mChar)];
	}
	return ret - minCnt[charToNum(mChar)];
}

///////////////

/////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////

static bool run()
{
	bool correct = false;
	int queryCnt;
	scanf("%d", &queryCnt);
	int H, W;
	char mChar;
	static char mStr[90001];

	while (queryCnt--)
	{
		int cmd;
		scanf("%d", &cmd);

		if (cmd == CMD_INIT)
		{
			scanf("%d %d %s", &H, &W, mStr);
			init(H, W, mStr);
			correct = true;
		}
		else if (cmd == CMD_INSERT)
		{
			scanf(" %c", &mChar);
			insert(mChar);
		}
		else if (cmd == CMD_MOVECURSOR)
		{
			int mRow, mCol;
			scanf("%d %d", &mRow, &mCol);

			char ret = moveCursor(mRow, mCol);

			char ans;
			scanf(" %c", &ans);
			if (ret != ans)
			{
				correct = false;
			}
		}
		else if (cmd == CMD_COUNT)
		{
			scanf(" %c", &mChar);

			int ret = countCharacter(mChar);

			int ans;
			scanf("%d", &ans);
			if (ret != ans)
			{
				correct = false;
			}
		}
	}
	return correct;
}

int main()
{
	setbuf(stdout, NULL);
	freopen("../input.txt", "r", stdin);

	int T, MARK;
	scanf("%d %d", &T, &MARK);

	for (int tc = 1; tc <= T; tc++)
	{
        if (tc == 2) {
            printf("debug");
        }
		int score = run() ? MARK : 0;
		printf("#%d %d\n", tc, score);
	}
	return 0;
}