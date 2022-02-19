#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

struct node {
    bool active = false;
    node *next[10];
    ~node() {
        for (int i = 0; i < 10; i++) {
            if (next[i]) delete next[i];
        }
    }
};

node* root;
bool addAndFind(char s[11]) {
    int slen = strlen(s);
    node *cur = root;

    for (int i = 0; i < slen; i++) {
        int num = s[i]-'0';
        if (!cur->next[num]) { cur->next[num] = new node(); }
        else if (i == slen-1) { return true; }
        cur = cur->next[num];

        if (cur->active) { return true; }
    }
    
    cur->active = true;
    return false;
}

void solve() {
    int n; scanf("%d", &n);
    root = new node();
    bool found = false;

    char line[11];
    for (int i = 0; i < n; i++) {
        scanf("%s", line);
        if (found) { continue; }
        found = addAndFind(line);
        if (found) { printf("NO\n"); }
    }
    if (!found) { printf("YES\n"); }
}

void testcase() {
    solve();
    delete root;
}

int main() {
    freopen("../input.txt", "r", stdin);
    setbuf(stdout, nullptr);
    int T; scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        testcase();
    }
}