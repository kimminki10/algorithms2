#include <iostream>
#include <string>

using namespace std;

string solve() {
    int N, M;
    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        if (!(M & (1<<i))) {
            return "OFF";
        }
    }

    return "ON";
}

void testcase(int tc) {
    cout << "#" << (tc+1) << " " << solve() << endl;
}

int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);

    int TC;
    cin >> TC;
    for (int i = 0; i < TC; i++) {
        testcase(i);
    }
}