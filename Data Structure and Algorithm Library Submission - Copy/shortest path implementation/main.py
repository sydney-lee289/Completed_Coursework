import sys


class Graph:
    def __init__(self, g): #2d list as input
        self.graph = g
        self.V = len(self.graph) #row i think?

    def shortestPath(self, s):
        minDist = [sys.maxsize] * self.V
        sptSet = set()
        minDist[s] = 0
        while(len(sptSet) != self.V):
            currentNode = -1
            min = sys.maxsize
            for n in range(self.V):
                if minDist[n] < min and n not in sptSet:
                    min = minDist[n]
                    currentNode = n
            if currentNode != -1:
                sptSet.add(currentNode)
                for nh in self.graph[currentNode]: #nh is neighbor i think
                    neighbor = nh[0]
                    cost = nh[1]
                    newDist = minDist[currentNode] + cost
                    if newDist < minDist[neighbor] and neighbor not in sptSet:
                        minDist[neighbor] = newDist
        print(minDist)

g = [[(1, 4), (7, 8)],
     [(0, 4), (2, 8), (7, 11)],
     [(1, 8), (3, 7), (8, 2), (5, 4)],
     [(2, 7), (5, 14), (4, 9)],
     [(3, 9), (5, 10)],
     [(4, 10), (3, 14), (2, 4), (6, 2)],
     [(5, 2), (7, 1), (8, 6)],
     [(6, 1), (8, 7), (1, 11), (6, 8)],
     [(2, 2), (6, 6), (7, 7)]]

G = Graph(g)
G.shortestPath(0)
G.shortestPath(3)