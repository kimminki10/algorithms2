#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void dodo(int l, string numBoard, int c, string &result) {
    if (l == c) { 
        if (result.compare(numBoard) < 0) {
            result = numBoard;
        }
        return; 
    }
    string nb(numBoard);
    int size = (int)nb.size();
    
    for (int i = l; i < size; i++) {
        for (int j = i+1; j < size; j++) {
            if (nb[j] >= nb[i]) {
                swap(nb[i], nb[j]);
                dodo(l+1, nb, c, result);
                swap(nb[i], nb[j]);
            }
        }
    }

    swap(nb[size-1], nb[size-2]);
    dodo(l+1, nb, c, result);
    swap(nb[size-1], nb[size-2]);
}

string solve() {
    string numBoard; 
    int changeCount;
    cin >> numBoard >> changeCount;
    string result = "0";

    dodo(0, numBoard, changeCount, result);
    return result;
}

void testcase(int tc) {
    string result = solve();
    cout << "#" << tc << " " << result << endl;
}
int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("../input.txt", "r", stdin);

    int T; cin>>T;
    for (int i = 0; i < T; i++) {
        testcase(i+1);
    }
}