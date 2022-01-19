#include <iostream>

using namespace std;

class BitSet {
public:
    int s = 0;
    int target = 0b111'111'1111;

    bool isSet(int n) {
        int bn = 1 << n;
        if ((s & bn) == bn) {
            return true;
        }
        return false;
    }

    void set(int n) {
        int bn = 1 << n;
        s = s | bn;
    }

    bool isSolved() {
        bool result = (s & target) == target;
        return result;
    }
};

void dodo(BitSet &bs, int i, int n) {
    int num = i * n;
    for (int x = num % 10; num > 0; num /= 10, x = num % 10) {
        bs.set(x);
    }
}

int solve() {
    int n; cin >> n;
    BitSet bs;
    for (int i = 1; ; i++) {
        if (i == 92) {
            break;
        }
        dodo(bs, i, n);
        if (bs.isSolved()) {return i*n;}
    }
    return 0;
}

void testcase(int t) {
    int result = 0;
    result = solve();
    cout << "#" << (t+1) << " " << result << endl;
}

int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    for (int i = 0; i < T; i++) {
        testcase(i);
    }
}