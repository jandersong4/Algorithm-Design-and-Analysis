import sys
from collections import defaultdict
import heapq

class Graph:
    def __init__(self,n,e):
        self.n = n
        self.e = e
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append([v, weight])
        self.graph[v].append([u,weight])
        
    def build_sources(self,sources):
        self.ambulance_cities = sources
        
    def dijkstra(self):
        distance = defaultdict(lambda: float('inf'))
        visited = defaultdict(bool)
        
        for u in self.graph:
            distance[u] = float('inf')
            visited[u] = False
        
        queue = []
        
        for s in self.ambulance_cities:
            distance[s] = 0
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
                    heapq.heappush(queue, (distance[v], v))
    
        return distance 

data = list(map(int, sys.stdin.buffer.read().split()))
# nome_arquivo = sys.argv[1]
# with open(nome_arquivo, "r") as arquivo:
#     data = list(map(int, arquivo.read().split()))

end_of_line =  False
index = 0

while not end_of_line:

    n = data[index]
    m = data[index+1]
    ambulance_cities_quantity = data[index+2]
    
    graph = Graph(n,m)
    
    sources = []

    index+=3
    
    for _ in range(m):
        u = data[index]
        v = data[index+1]
        w = data[index+2]
        
        graph.add_edge(u,v,w)
        
        index+=3

    for _ in range(ambulance_cities_quantity):
        ambulance_city = data[index]
        sources.append(ambulance_city)
        index+=1
    
    graph.ambulance_cities = sources

    try:
        data[index+1]
    except:
        end_of_line = True
    
    # print(graph.graph)
    # print(graph.ambulance_cities)
    distances = graph.dijkstra()
    print(max(distances.values())) 
    