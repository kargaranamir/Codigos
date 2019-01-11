#include <iostream>
#include <vector>
#include <bitset>
using namespace std;
vector<int> graph(50032), unvisitedited(50032, -1);
bitset<50032> visited;
int DFS(int u) {
  if (visited[u])return 1;
  visited[u] = 1;
  unvisitedited[u] = 1 + DFS(graph[u]);
  visited[u] = 0;
  return unvisitedited[u];
}
int T, Node_num, counter = 0;
int main() {
  cin >> T;
  if (T>20)
    return 0;
  while (counter++<T) {
    cin >> Node_num;
    if (Node_num > 50000 || Node_num<2)
      return 0;
    visited.reset();
    for (int i = 1; i <= Node_num; i++) {
      int x, y;
      cin >> x >> y;
      graph[x] = y;
      unvisitedited[x] = 0;
    }
    int answer = 0, point = 0;
    for (int i = 1; i <= Node_num; i++) {
      if (!unvisitedited[i])DFS(i);
      if (unvisitedited[i]>point)
        point = unvisitedited[i], answer = i;
    }
    cout << "Case " << counter << ": " << answer << endl;
  }
}