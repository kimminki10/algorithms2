#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long ll;
const int MAX_S = 500'001;
const int MAX_W = 100'001;

int fail[MAX_W]={0,};

void fail_function(char *W, int M) {
    for (int i=1,j=0;i<M;i++) {
        while(j>0&&W[i]!=W[j]) j = fail[j-1];
        if (W[i]==W[j]) fail[i] = ++j;
    }
}

int kmp(char *S, int N, char *W, int M) {
    int ret = 0;
    for (int i = 0,j=0;i<N; i++) {
        while(j>0&&S[i]!=W[j]) { j = fail[j-1]; }
        if (S[i] == W[j]) {
            if (j==M-1) {
                ret++;
                j = fail[j];
            } else { j++; }
        }
    }
    return ret;
}

void solve() {
    char S[MAX_S] = {0,};
    char W[MAX_W] = {0,};

    scanf(" %[^\n]", S);
    scanf(" %[^\n]", W);
    int N = strlen(S);
    int M = strlen(W);

    
    fail_function(W, M);

    printf("%d\n", kmp(S, N, W, M));
}

void testcase(int tc) {
    memset(fail,0,sizeof(fail));
    printf("#%d ", tc);
    solve();
}

int main() {
    freopen("../input.txt", "r", stdin);
    setbuf(stdout, nullptr);
    int T; scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}