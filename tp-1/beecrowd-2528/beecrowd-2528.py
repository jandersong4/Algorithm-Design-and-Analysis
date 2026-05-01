import sys
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def remove_e(self, e):
        if self.graph[e]:
            self.graph[e].clear()
        for node in self.graph:
            neighbors = self.graph[node]
            if e in neighbors:
                self.graph[node].remove(e)
            
    def BFS(self,s,t):
        visited = defaultdict(list)
        distance = defaultdict(list)
        
        for u in self.graph:
            visited[u] = False
            distance[u] = 0
    
        visited[s] = True
        
        queue = deque()
        queue.append(s)
        
        path_done = False
        while queue and (not path_done):
            u = queue.popleft()
            neighbors = self.graph[u]
            for v in neighbors:
                if not visited[v]:
                    visited[v] = True   
                    distance[v] = distance[u] + 1
                    queue.append(v)
                    if v == t: 
                        path_done = True
                        break
        
        return distance[t]       

data = list(map(int, sys.stdin.buffer.read().split()))

end_of_lines = False

index = 0
while not end_of_lines:
    graph = Graph()
    
    n = data[index]
    e = data[index+1]
    index+=2
    
    for edges in range(e):
        u = data[index]
        v = data[index+1]
        graph.add_edge(u,v)
        index+=2
    
    c = data[index]
    r = data[index+1]
    e = data[index+2]
    index+=3
        
    try:
        data[index+1]
    except:
        end_of_lines = True
    
    graph.remove_e(e)
    distance = graph.BFS(c,r)
    print(distance)