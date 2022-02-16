#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long ll;

const ll base = 251;
const ll MOD = 1e9+7;

ll sub_w = 1;

char word[2001][2001];
char source[2001][2001];

ll hashW[2000];
ll hashS[2000];

ll hash_func(char *s, int start, int end) {
    ll hash = 0;
    for (int i = start; i < end; i++) {
        hash = (hash*base + s[i]) % MOD;
    }
    return hash;
}

ll next_hash(ll prev_hash, char* s, int start, int end, ll sub_v) {
    ll hash = ((prev_hash- (s[start-1] * sub_v) %MOD) +MOD) %MOD;
    hash = (hash*base + s[end-1]) %MOD;
    return hash;
}

int H, W, N, M;
ll fail[2000];
void fail_function(ll lines[2000]) {
    for (int i=1,j=0 ;i < H; i++) {
        while (j>0&& hashW[i] != hashW[j]) j = fail[j-1];
        if (hashW[i] == hashW[j]) { fail[i] = ++j; }
    }
}

int kmp() {
    int result = 0;
    for (int i = 0, j = 0; i < N; i++) {
        while (j > 0 && hashS[i] != hashW[j]) { j = fail[j-1]; }
        if (hashS[i] == hashW[j]) {
            if (j == H-1) {
                result++;
                j = fail[j];
            } else j++;
        }
    }
    return result;
}

void solve() {
    scanf("%d %d %d %d", &H, &W, &N, &M);

    for (int i = 0; i < W-1; i++) { sub_w = (sub_w * base) % MOD; }

    for (int i = 0; i < H; i++) { scanf("%s", word[i]); }
    for (int i = 0; i < N; i++) { scanf("%s", source[i]); }
    
    for (int i = 0; i < H; i++) { hashW[i] = hash_func(word[i], 0, W); }
    for (int i = 0; i < N; i++) { hashS[i] = hash_func(source[i], 0, W); }

    fail_function(fail);
    int result = kmp();
    for (int j = 1; j <= M-W; j++) {
        for (int i = 0; i < N; i++) {
            hashS[i] = next_hash(hashS[i], source[i], j, j+W, sub_w);
        }
        result += kmp();
    }
    printf("%d\n", result);
}

void testcase(int tc) {
    memset(fail, 0, sizeof(fail));
    memset(hashS, 0, sizeof(hashS));
    memset(hashW, 0, sizeof(hashW));
    sub_w = 1;

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