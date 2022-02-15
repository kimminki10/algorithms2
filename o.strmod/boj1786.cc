#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;
const int MAX_S = 1'000'001;

void fail_function(char *W, int M, int fail[MAX_S]) {
    for (int i=1, j=0; i < M; i++) {
        while(j>0 && W[i] != W[j]) 
            j = fail[j-1];
        if (W[i] == W[j]) fail[i] = ++j;
    }
}

vector<int> kmp(char* S, int N, char* W, int M, int fail[MAX_S]) {
    vector<int> ret;
    for (int i=0,j=0; i < N; i++) {
        while(j>0&& S[i] != W[j]) j=fail[j-1];
        if (S[i] == W[j]) {
            if (j == M-1) {
                ret.push_back(i-M+2);
                j = fail[j];
            } else j++;
        }
    }
    return ret;
}

int main() {
    setbuf(stdout, nullptr);
    freopen("../input.txt", "r", stdin);

    char T[MAX_S]={0,};
    char P[MAX_S]={0,};

    scanf(" %[^\n]", T);
    scanf(" %[^\n]", P);

    int N = strlen(T);
    int M = strlen(P);

    int fail[MAX_S] = {0,};

    fail_function(P, M, fail);
    vector<int> matched = kmp(T, N, P, M, fail);

    printf("%d\n", (int)matched.size());
    for (int i : matched) {
        printf("%d ", i);
    }
}