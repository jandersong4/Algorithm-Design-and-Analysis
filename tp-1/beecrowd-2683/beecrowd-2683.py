import sys
import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append([v, weight])
        self.graph[v].append([u, weight])    
    
    def prim(self, r, maximize=False):
        key = defaultdict(list)
        visited = defaultdict(list)
        
        for node in self.graph:
            if maximize:
                key[node] = float('-inf')
            else:
                key[node] = float('inf')
            visited[node] = False
        
        key[r] = 0
        total_cost = 0
        queue = []
                    
        heapq.heappush(queue, (0, r))
        
        while queue:
            current_weight, u = heapq.heappop(queue)
            
            if visited[u] ==  True:
                continue
            
            visited[u] = True
            total_cost += key[u]
            
            
            for v,weight in self.graph[u]:
                if visited[v] == False:
                    if (not maximize and weight < key[v]) or (maximize and weight > key[v]):
                        key[v] = weight
                        if maximize:
                            heapq.heappush(queue, (-key[v], v))
                        else:
                            heapq.heappush(queue, (key[v], v))
        return total_cost
    

data = list(map(int, sys.stdin.buffer.read().split()))

graph = Graph()

gallery_quantity = int(data[0])

index = 1
for gallery in range(gallery_quantity):
    u = int(data[index])
    v = int(data[index+1])
    weight = int(data[index+2])
    graph.add_edge(u,v,weight)
    index+=3
    
min_spanning_tree_costs = graph.prim(1)
max_spanning_tree_costs = graph.prim(1,maximize=True)

print(max_spanning_tree_costs)
print(min_spanning_tree_costs)
    
