#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>
#include <ctime>
/////
struct post {
    int like=0;
    int uid=-1;
    int timestamp;
} posts[100'005];
int postCnt = 0;

int following[1'003][1'003];
int fidx[1'003];

int userNum;
void init(int N) {
    userNum = N;
    postCnt = 0;
    for (int i = 0; i <= N; i++) { 
        following[i][0] = i; 
        fidx[i] = 1;
    }
}

void follow(int uID1, int uID2, int timestamp) {
    int fi = fidx[uID1]++;
    following[uID1][fi] = uID2;
}

void makePost(int uID, int pID, int timestamp) {
    postCnt++;
    post &p = posts[pID];
    p.like = 0; p.uid = uID; p.timestamp = timestamp;
}

void like(int pID, int timestamp) {
    posts[pID].like++;
}

bool isFollow(int uID, int puid) {
    int fl = fidx[uID];
    for (int i = 0; i < fl; i++) {
        if (following[uID][i] == puid) {
            return true;
        }
    }
    return false;
}

void getFeed(int uID, int timestamp, int pIDList[]) {
    int topten[11];
    int tidx = 0;
    for (int pid = postCnt; pid >= 1; pid--) {
        post p = posts[pid];
        if (!isFollow(uID, p.uid)) { continue; }

        if (timestamp - p.timestamp > 1000) {
            if (tidx >= 10) { break; }
            topten[tidx++] = pid;
            if (tidx >= 10) { break; }
            continue;
        }

        int cur = 0;
        for (; cur < tidx; cur++) {
            int tid = topten[cur];
            if (posts[tid].like < posts[pid].like) {
                for (int i = tidx; i >= cur+1; i--) {
                    topten[i] = topten[i-1];
                }
                break;
            }
        }
        topten[cur] = pid; tidx++;
        if (tidx > 10) { tidx = 10; }
    }

    for (int i = 0; i < 10; i++) {
        pIDList[i] = topten[i];
    }
}

/////
static int mSeed;
static int pseudo_rand(void) {
    mSeed = mSeed * 431345 + 2531999;
    return mSeed & 0x7FFFFFFF;
}

static int follow_status[1005][1005];
static int answer_score;
static int n;  // n >= 2 && n <= 1000
static int end_timestamp;
static int follow_ratio;    // follow_ratio >= 1 && follow_ratio <= 10000
static int make_ratio;      // make_ratio >= 1 && make_ratio <= 10000
static int like_ratio;      // like_ratio >= 1 && like_ratio <= 10000
static int get_feed_ratio;  // get_feed_ratio >= 1 && get_feed_ratio <= 10000
static int post_arr[200000];
static int total_post_cnt;
static int min_post_cnt;

static bool run() {
    int uId1, uId2, pId, pIdList[10], ans_pIdList[10], rand_val;
    bool ret = true;

    scanf("%d%d%d%d%d%d%d", &mSeed, &n, &end_timestamp, &follow_ratio,
          &make_ratio, &like_ratio, &get_feed_ratio);
    init(n);

    for (int uId1 = 1; uId1 <= n; uId1++) {
        follow_status[uId1][uId1] = 1;
        int m = n / 10 + 1;
        if (m > 10) m = 10;
        for (int i = 0; i < m; i++) {
            uId2 = uId1;
            while (follow_status[uId1][uId2] == 1) {
                uId2 = pseudo_rand() % n + 1;
            }
            follow(uId1, uId2, 1);
            follow_status[uId1][uId2] = 1;
        }
    }
    min_post_cnt = total_post_cnt = 1;

    for (int timestamp = 1; timestamp <= end_timestamp; timestamp++) {
        rand_val = pseudo_rand() % 10000;
        if (rand_val < follow_ratio) {
            uId1 = pseudo_rand() % n + 1;
            uId2 = pseudo_rand() % n + 1;
            int lim = 0;
            while (follow_status[uId1][uId2] == 1 || uId1 == uId2) {
                uId2 = pseudo_rand() % n + 1;
                lim++;
                if (lim >= 5) break;
            }
            if (follow_status[uId1][uId2] == 0) {
                follow(uId1, uId2, timestamp);
                follow_status[uId1][uId2] = 1;
            }
        }
        rand_val = pseudo_rand() % 10000;

        if (rand_val < make_ratio) {
            uId1 = pseudo_rand() % n + 1;
            post_arr[total_post_cnt] = timestamp;

            makePost(uId1, total_post_cnt, timestamp);
            total_post_cnt += 1;
        }

        rand_val = pseudo_rand() % 10000;

        if (rand_val < like_ratio && total_post_cnt - min_post_cnt > 0) {
            while (post_arr[min_post_cnt] < timestamp - 1000 &&
                   min_post_cnt < total_post_cnt)
                min_post_cnt++;

            if (total_post_cnt != min_post_cnt) {
                pId = pseudo_rand() % (total_post_cnt - min_post_cnt) +
                      min_post_cnt;
                like(pId, timestamp);
            }
        }

        rand_val = pseudo_rand() % 10000;
        if (rand_val < get_feed_ratio && total_post_cnt > 0) {
            uId1 = pseudo_rand() % n + 1;
            getFeed(uId1, timestamp, pIdList);

            for (int i = 0; i < 10; i++) {
                scanf("%d", ans_pIdList + i);
            }

            for (int i = 0; i < 10; i++) {
                if (ans_pIdList[i] == 0) break;

                if (ans_pIdList[i] != pIdList[i]) {
                    ret = false;
                }
            }
        }
    }

    return ret;
}

int main() {
    clock_t start, end;
    freopen("../input.txt", "r", stdin);
    setbuf(stdout, NULL);
    int tc;
    start = clock();
    scanf("%d%d", &tc, &answer_score);

    for (int t = 1; t <= tc; t++) {
        int score;
        for (int i = 0; i < 1005; i++)
            for (int j = 0; j < 1005; j++) follow_status[i][j] = 0;

        if (run())
            score = answer_score;
        else
            score = 0;

        printf("#%d %d\n", t, score);
    }
    end = clock();
    printf("time: %lf sec\n", (double)(end-start) / CLOCKS_PER_SEC);
    return 0;
}