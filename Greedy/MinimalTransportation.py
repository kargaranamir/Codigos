import math

class Countiner:
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0 for i in range(0, N)]
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def Set(self, i, j):
        if not self.find(i) == self.find(j):
            x = self.find(i)
            y = self.find(j)
            if self.rank[x] > self.rank[y]:
                self.parent[y] = x
            else:
                self.parent[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1


def kruskal(N, R, edges):
    roads = 0 ; rails = 0 ;states = 0
    cs = Countiner(N)
    for edge in edges:
        if not cs.find(edge[1]) == cs.find(edge[2]):
            cs.Set(edge[1], edge[2])
            if(edge[0] <= R):
                roads += edge[0]
            else:
                states += 2 if states == 0 else 1
                rails += edge[0]
    if states == 0: 
        states = 1
    return states, roads, rails



def main():
    T = int(input())
    for C in range(T):
        N, R = map(int, input().split())
        V = []
        edges = []
        for i in range(0, N):
            x, y = map(int, input().split())         
            V.append((x, y))
            for j in range(0, i):
                distance = math.sqrt(((V[i][0]-V[j][0])**2) + ((V[i][1]- V[j][1])**2))
                edges.append((distance, i, j))
                edges.sort()
        states, roads, rails = kruskal(N, R, edges)
        roads = math.floor(roads + 0.5)
        rails = math.floor(rails + 0.5)
        s = "Case #" + str(C+1) + ': ' + ' '.join([str(i) for i in [states, roads, rails]])
        print(s)

if __name__ == '__main__': 
    main()
