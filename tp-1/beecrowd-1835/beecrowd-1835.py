import sys
from collections import defaultdict, deque

class Graph_input:
    def __init__(self, node_count, edge_count, edges_list):
        self.node_count = node_count
        self.edge_count = edge_count
        self.edge_list = edges_list

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def BFS(self,s):
        visited = defaultdict(list)
        
        for u in self.graph:
            visited[u] = False
    
        visited[s] = True
        
        queue = deque()
        queue.append(s)
        
        while queue:
            u = queue.popleft()
            neighbors = self.graph[u]
            for v in neighbors:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        
        found_nodes = [key for key, value in visited.items() if value is True]
        return found_nodes
    

tokens = sys.stdin.read().split()
tokens = [token for token in tokens if token.isdigit()]

test_case_list = []

test_count = int(tokens[0])
index = 1

for _ in range(test_count):
    node_count = int(tokens[index])
    index += 1

    edge_count = int(tokens[index])
    index += 1

    graph_input = Graph_input(node_count, edge_count, [])

    for _ in range(edge_count):
        u = tokens[index]
        v = tokens[index + 1]
        index += 2

        graph_input.edge_list.append(f"{u} {v}")

    test_case_list.append(graph_input)
    
case = 1
for test in test_case_list:
    graph = Graph()
    n = test.node_count
    
    for edge in test.edge_list:
        u, v = map(int, edge.split())
        graph.add_edge(u,v)
    
    not_visited_nodes = list(range(1,n+1))

    forest_list = []

    while not_visited_nodes:
        s = not_visited_nodes.pop(0)
        forest = graph.BFS(s)
        forest_list.append(forest)
        not_visited_nodes = [item for item in not_visited_nodes if item not in forest]

    if len(forest_list) == 1:
        print('Caso #{}: a promessa foi cumprida'.format(case))
        case+=1
    else:
        print('Caso #{}: ainda falta(m) {} estrada(s)'.format(case, len(forest_list) - 1))
        case+=1
    