import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self):
        # self.n = n
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def Kosaraju(self):
        visited = defaultdict(list)
        # visited = [False] * (self.n+1)
        for u in self.graph:
            visited[u] = False
        
        dfs_stack_order = []
        
        for u in self.graph:
            if visited[u] == False:
                self.dfs_order(u, visited, dfs_stack_order)
                
        transposed_graph = self.transpose_graph()
        
        for u in self.graph:
            visited[u] = False
        
        components_list = []
        
        while dfs_stack_order:
            u = dfs_stack_order.pop()
            
            if visited[u] == False:
                component = []
                self.build_component(transposed_graph, u, visited, component)
                components_list.append(component)
        
        return components_list
                
    
    def dfs_order(self, u, visited, dfs_stack_order):
        visited[u] = True
        neighbors = self.graph[u]
        
        for v in neighbors:
            if visited[v] == False:
                self.dfs_order(v, visited, dfs_stack_order)
        dfs_stack_order.append(u)
        
    def transpose_graph(self):
        transpose_graph = Graph()
        for u in self.graph:
            neighbors = self.graph[u]
            for v in neighbors:
                transpose_graph.add_edge(v,u)
        return transpose_graph
    
    def build_component(self, transposed_graph, u, visited, component):
        visited[u] = True
        component.append(u)
        
        neighbors = transposed_graph.graph[u]
        for v in neighbors:
            if visited[v] == False:
                self.build_component(transposed_graph, v, visited, component)
        
data = list(map(int, sys.stdin.buffer.read().split()))

cities_count = data[0]
graph = Graph()

index = 1
while index < len(data):
    u = data[index]
    v = data[index+1]
    
    graph.add_edge(u,v)
    index+=2

forests = graph.Kosaraju()

if len(forests) == 1:
    if(len(forests[0]) == cities_count):
        print('S')
elif len(forests) > 1:
    print('N') 

