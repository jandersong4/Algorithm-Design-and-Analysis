import sys
from collections import defaultdict
import heapq

class Graph:
    def __init__(self,n,e):
        self.n = n
        self.e = e
        self.graph = defaultdict(list)

        for i in range(n):
            self.graph[i]

    def add_edge(self, u, v, weight):
        self.graph[u].append([v, weight])

    def dijkstra(self,s,t):
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
            if u == t:
                return self.build_path(father, s, t)
            
            neighbors = self.graph[u]
            for v,weight in neighbors:
                if distance[v] > (distance[u] + weight):
                    distance[v] = (distance[u] + weight)
                    father[v] = [u,weight]
                    heapq.heappush(queue, (distance[v], v))
                    
        return False
    
    def build_path(self,father,s,t):
        current_node = t
        cost = 0
        while (current_node != s):
            parent,weight=father[current_node]
            cost+=weight
            current_node=parent
        return cost

    def Kosaraju(self):
        visited = [False] * (self.n + 1)
        dfs_stack_order = []
        
        for u in range(1, self.n + 1):
            if visited[u] == False:
                self.dfs_order(u, visited, dfs_stack_order)
                
        transposed_graph = self.transpose_graph()
        visited = [False] * (self.n + 1)
        components_list = []
        
        while dfs_stack_order:
            u = dfs_stack_order.pop()
            
            if visited[u] == False:
                component = []
                self.build_component(transposed_graph, u, visited, component)
                self.zero_internal_edges(component)
                components_list.append(component)

        return components_list         

    def dfs_order(self, u, visited, dfs_stack_order):
        visited[u] = True
        neighbors = self.graph[u]
        
        for v, weight in neighbors:
            if visited[v] == False:
                self.dfs_order(v, visited, dfs_stack_order)
        dfs_stack_order.append(u)

    def transpose_graph(self):
        transpose_graph = Graph(self.n, self.e)
        for u in range(1, self.n + 1):
            neighbors = self.graph[u]
            for v,weight in neighbors:
                transpose_graph.add_edge(v,u,weight)
        return transpose_graph

    def build_component(self, transposed_graph, u, visited, component):
        visited[u] = True
        component.append(u)
        
        neighbors = transposed_graph.graph[u]
        for v, weight in neighbors:
            if visited[v] == False:
                self.build_component(transposed_graph, v, visited, component)

    def zero_internal_edges(self, component):
        component_set = set(component)

        for u in component_set:
            for edge in self.graph[u]:
                v = edge[0]
                
                if v in component_set:
                    edge[1] = 0

data = list(map(int, sys.stdin.buffer.read().split()))
# nome_arquivo = sys.argv[1]

# with open(nome_arquivo, "r") as arquivo:
#     data = list(map(int, arquivo.read().split()))
    
end_of_data = False
index =  0

while not end_of_data:
    n = data[index]
    e = data[index+1]
    graph = Graph(n,e)
    
    index+=2
    for edges in range(e):
        u = data[index]
        v = data[index+1]
        weight = data[index+2]
        graph.add_edge(u,v,weight)
        index+=3
    
    strong_conected_components = graph.Kosaraju()
    
    trials = data[index]
    index+=1
    for test in range(trials):
        city_u = data[index]
        city_v = data[index+1]
        
        same_country = False
        for component in strong_conected_components:
            if (city_u in component and city_v in component):
                same_country = True

        if same_country:
            print(0)
        else:
            if graph.dijkstra(city_u,city_v):
                print(graph.dijkstra(city_u,city_v))
            else:
                print('Nao e possivel entregar a carta')
        index+=2
    print()
        
    if data[index] == 0 and data[index+1] == 0:
        break