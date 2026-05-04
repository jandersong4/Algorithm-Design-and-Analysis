import sys
from collections import defaultdict
import heapq

sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self,n,e):
        self.n = n
        self.e = e
        self.graph = defaultdict(list)
        self.cycles = []
        

    def add_edge(self, u, v, weight):
        self.graph[u].append([v, weight])
        self.graph[v].append([u,weight])
        
    def DFS(self, start):
        visited = defaultdict(bool)
        father = defaultdict(lambda: None)
        father_weight = defaultdict(int)
        depness = defaultdict(int)
        distance = defaultdict(int)

        cycles = []

        def dfs_visit(u):
            visited[u] = True

            for v, w in self.graph[u]:
                if not visited[v]:
                    father[v] = u
                    father_weight[v] = w
                    depness[v] = depness[u] + 1
                    distance[v] = distance[u] + w

                    dfs_visit(v)

                elif v != father[u] and depness[v] < depness[u]:
                    length = distance[u] - distance[v] + w

                    nodes = []
                    current_node = u

                    while current_node != v:
                        nodes.append(current_node)
                        current_node = father[current_node]

                    nodes.append(v)

                    cycles.append((nodes, length))

        father[start] = None
        depness[start] = 0
        distance[start] = 0

        dfs_visit(start)

        self.cycles = cycles
    
    def dijkstra(self,s):
        distance = defaultdict(list)
        father = defaultdict(list)
        visited = defaultdict(list)
        
        for u in self.graph:
            distance[u] = float('inf')
            father[u] = None
            visited[u] = False
            
        distance[s] = 0
        queue = []
        heapq.heappush(queue, (0, s))
                
        while queue:
            current_distance, u = heapq.heappop(queue)
            if visited[u]:
                continue
            visited[u] = True
            
            neighbors = self.graph[u]
            for v,weight in neighbors:
                if distance[v] > (distance[u] + weight):
                    distance[v] = (distance[u] + weight)
                    father[v] = [u,weight]
                    heapq.heappush(queue, (distance[v], v))
                    
        return distance
    
    def try_path(self, source, worm_length, cycles):
        INF = 10**18
        
        distance = self.dijkstra(source)
        answer = INF
        
        for nodes, cycle_length in self.cycles:
            if cycle_length >= worm_length:
                cycle_distance = INF
                
                for node in nodes:
                    cycle_distance = min(cycle_distance, distance[node])
                    
                if cycle_distance != INF:
                    candidate = 2 * cycle_distance + cycle_length
                    answer = min(answer, candidate)
        
        if answer == INF:
            return -1
    
        return answer
            

data = list(map(int, sys.stdin.buffer.read().split()))

end_of_line =  False
index = 0

while not end_of_line:

    n = data[index]
    m = data[index+1]
    
    graph = Graph(n,m)
    
    index+=2
    
    for _ in range(m):
        u = data[index]
        v = data[index+1]
        w = data[index+2]
        
        graph.add_edge(u,v,w)
        
        index+=3

    trials = data[index]
    
    index +=1
    
    graph.DFS(1)
    cycles = graph.cycles

    for _ in range(trials):
        source = data[index]
        worm_length = data[index+1]
        
        index +=2
        
        print(graph.try_path(source,worm_length,cycles))

    try:
        data[index+1]
    except:
        end_of_line = True
    
    