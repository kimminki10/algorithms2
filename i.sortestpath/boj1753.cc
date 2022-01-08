#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int INF = 987654321;
int V, E, K;
vector<pair<int, int> > g[20'001];

vector<int> dijkstra(int s, int v_num) {
    vector<int> distance(v_num, INF);
    distance[s] = 0;

    priority_queue< pair<int, int> > pq;
    pq.push({0, s});

    while(!pq.empty()) {
        int cost = -pq.top().first;
        int curV = pq.top().second;
        pq.pop();

        if (distance[curV] < cost) { continue; }

        for (int i = 0; i < (int)g[curV].size(); i++) {
            int n = g[curV][i].first;
            int nd = cost + g[curV][i].second;

            if (distance[n] > nd) {
                distance[n] = nd;
                pq.push({-nd, n});
            }
        }
    }
    return distance;
}

int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> V >> E;
    cin >> K;

    for (int i = 0; i < E; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        g[u].push_back({v, w});
    }
    auto result = dijkstra(K, V+1);
    for (int i = 1; i <= V; i++) {
        if (result[i] == INF) {
            cout << "INF\n";
        } else {
            cout << result[i] << "\n";
        }
    }

}