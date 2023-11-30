class Graph:
    def __init__(self, n):
        self.graph = dict()
        for i in range(n):
            self.graph[i] = [] # giving all the nodes keys, then giving each a list

    def addEdge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].append(v)

    def DFS(self, u):
        visited = [False] * len(self.graph.keys())
        self.DFSInternal(u, visited)

    def DFSInternal(self, u, visited):
        visited[u] = True
        print(u, end= ' ')
        for neighbor in self.graph[u]:
            if visited[neighbor] == False:
                self.DFSInternal(neighbor, visited)
    def BFS(self, u):
        visited = [False] * len(self.graph.keys())
        v = []
        visited[u] = True
        v.append(u)
        while(len(v) != 0):
            node = v.pop(0)
            print(node, end= ' ')
            for neighbor in self.graph[node]:
                if visited[neighbor] == False:
                    visited[neighbor] = True
                    v.append(neighbor)

    def BFSLevelSums(self, u):
        visited = [False] * len(self.graph.keys())
        q = []
        visited[u] = True
        q.append((u, 0))
        p = dict()
        while (len(q) != 0):
            v = q.pop(0)
            node = v[0]
            level = v[1]
            #print(node, end=' ')
            if level in p.keys():
                p[level] += node
            else:
                p[level] = node

            for neighbor in self.graph[node]:
                if visited[neighbor] == False:
                    visited[neighbor] = True
                    q.append((neighbor, level + 1))
        R = []
        for key in p.keys():
            R.append(p[key])
        return R




g = Graph(8)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(0,6)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(3,2)
g.addEdge(3,4)
g.addEdge(6,7)
g.addEdge(2,4)
g.addEdge(4,5)

g.DFS(0)
print()
g.DFS(1)
print()
g.BFS(0)
print()
g.BFS(1)
print()
print(g.BFSLevelSums(0))
print()
print(g.BFSLevelSums(1))