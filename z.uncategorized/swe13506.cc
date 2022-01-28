// Title : 범인 색출, Score 를 최소화하라
// 20 초
// stack Memory : 1M  (전역 변수 사용 금지)

#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>
#include <time.h>

#include <random>

const int MAX_NUM = 1000000;
static int SCORE, TOTAL_SCORE, TOTAL_TIME;
static char citizen[MAX_NUM];
static char room[MAX_NUM];
static char arrested[MAX_NUM];

void putIn(int n, int a) {
    if (n < 0 || n >= MAX_NUM) {
        printf("putin error\n");
        return;
    }
    if (a < 0 || a >= MAX_NUM) {
        printf("putin error\n");
        return;
    }
    room[n] |= citizen[a];
}

int closeDoor(int n) {
    SCORE += 1;
    if (n < 0 || n >= MAX_NUM) {
        printf("closeDoor error\n");
        return 0;
    }
    return room[n];
}

void clearRoom() {
    for (int i = 0; i < MAX_NUM; i++) room[i] = 0;
}

void arrest(int a) {
    SCORE += 10;
    if (a < 0 || a >= MAX_NUM) {
        printf("arrest error\n");
        return;
    }
    if (citizen[a] == 0) 
        SCORE += 10000;
    arrested[a] = 1;
}

//////

void binInvest(int l, int r, int d, bool* t, int max, int &found) {
    if (found >= 1000) { return; }

    int m = (l + r) / 2;
    printf("binInv l: %d, m: %d, r: %d\n", l, m, r);

    if (d > 500000) {
        for (int i = l; i < m; i++) {
            
            t[i] = true;
            found++;
        }

        for (int i = m; i < r; i++) {

        }
        return;
    }


    for (int i = l; i < m; i++) {
        putIn(2 * d, i);
    }
    for (int i = m; i < r; i++) {
        putIn(2 * d + 1, i);
    }

    if (closeDoor(2 * d)) {
        if (m-l == 1) { 
            //arrest(l); 
            t[l] = 1;
            return;
        }
        binInvest(l, m, 2 * d, t, max, found);
    }
    if (closeDoor(2 * d + 1)) {
        if (r-m == 1) { 
            //arrest(m); 
            t[m] = 1;
            return;
        }
        binInvest(m, r, 2 * d + 1, t, max, found);
    }
}

 /////
    // int found = 0;
    // binInvest(1, MAX_NUM, 2, st, max, found);
    // return;
//////

void investigate() { 
    int d = 2;
    int l, r;
    bool* st = new bool[4*MAX_NUM];
    for (int i = 0; i < 4*MAX_NUM; i++) { st[i]=false; }
    st[0] = 1;
    st[1] = 1;
    
    int max = 1; 
    for (; max < MAX_NUM; max *= 2) {}

    while (d <= max) {
        for (int d_i = 0; d_i < d; d_i++) {
            l = (max / d) * d_i;
            r = (max / d) * (d_i + 1);
            r = r > MAX_NUM ? MAX_NUM:r;

            for (int i = l; i < r; i++) { putIn(d_i, i); }
            if (r == MAX_NUM) break;
        }

        for (int i = 0; i < d; i++) {
            if (st[(d+i)/2] == 0) continue;
            st[d+i] = closeDoor(i);
        }
        d *= 2;
        clearRoom();
    }
    d /= 2;
    for (int i = 0; i < MAX_NUM; i++) {
        if (st[d+i] == 1) {
            putIn(i, i);
            arrest(i);
        }
    }
}
//////

static unsigned long long seed = 113;
std::random_device rd;
std::mt19937 gen(seed);
std::uniform_int_distribution<int> dis(0, MAX_NUM - 1);

void init() {
    SCORE = 0;
    for (int i = 0; i < MAX_NUM; i++) {
        citizen[i] = 0;
        room[i] = 0;
        arrested[i] = 0;
    }
    int j;
    for (int i = 0; i < MAX_NUM / 1000; i++) {
        j = dis(gen);
        if (citizen[j] == 1) {
            i--;
            continue;
        }
        citizen[j] = 1;
    }
}

int main() {
    int TC;
    TOTAL_SCORE = TOTAL_TIME = 0;
    freopen("../input.txt", "r", stdin);
    scanf("%d", &TC);
    for (int t = 1; t <= TC; t++) {
        init();
        investigate();
        for (int i = 0; i < MAX_NUM; i++)
            if (citizen[i] == 1 && arrested[i] == 0) SCORE += 90000;
        if (SCORE < 86400)
            printf("#%d 100 %d\n", t, SCORE);
        else
            printf("#%d 0 0\n", t);
        TOTAL_SCORE += SCORE;
    }
    printf("TOTAL SCORE : %d\n", TOTAL_SCORE);
}