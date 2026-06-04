import sys
from collections import defaultdict
from collections import deque

class Flights:

    def __init__(self, airports):
        self.airports = airports
        self.graph = defaultdict(list)

    def add_adges(self, u, v, empty_accent):
        self.graph[u].append([v,empty_accent])
        
    def expand_graph(self, day):
        previous_day = day - 1
        for u in range(1,self.airports + 1):
            current_edges = self.graph[(u, previous_day - 1)]
            new_edges_list = []
            for edge in current_edges:
                aux_list = list(edge[0])
                aux_list[1] += 1 
                new_edge = edge.copy()
                new_edge[0] = tuple(aux_list)
                new_edges_list.append(new_edge)
            self.graph[(u,previous_day)] = new_edges_list
            
    
    def build_residual_graph(self, graph):
        residual_graph = defaultdict(dict)

        for u, edges in graph.items():
            for v, capacity in edges:
                if capacity > 0:
                    residual_graph[u][v] = residual_graph[u].get(v, 0) + capacity

        return residual_graph


    def find_augmenting_path_bfs(self, graph, s, t):
        parent = {s: None}
        bottleneck = {s: float("inf")}

        queue = deque()
        queue.append(s)

        while queue:
            u = queue.popleft()

            for v, capacity in graph.get(u, {}).items():
                if capacity > 0 and v not in parent:
                    parent[v] = u
                    bottleneck[v] = min(bottleneck[u], capacity)

                    if v == t:
                        return parent, bottleneck[v]

                    queue.append(v)

        return None, 0


    def get_capacity(self, graph, u, v):
        for neighbor, capacity in graph[u]:
            if neighbor == v:
                return capacity

        return 0


    def ford_fulkerson(self, source, sink, limit):
        residual_graph = self.build_residual_graph(self.graph)

        max_flow = 0

        parent, bottleneck = self.find_augmenting_path_bfs(
            residual_graph, source, sink
        )

        while parent is not None and max_flow < limit:
            if max_flow + bottleneck > limit:
                bottleneck = limit - max_flow

            max_flow += bottleneck

            v = sink
            while v != source:
                u = parent[v]

                residual_graph[u][v] -= bottleneck

                if residual_graph[u][v] == 0:
                    del residual_graph[u][v]

                residual_graph[v][u] = residual_graph[v].get(u, 0) + bottleneck

                v = u

            parent, bottleneck = self.find_augmenting_path_bfs(
                residual_graph, source, sink
            )

        return max_flow
            
        
data = list(map(int, sys.stdin.buffer.read().split()))
# nome_arquivo = sys.argv[1]
# with open(nome_arquivo, "r") as arquivo:
#     data = list(map(int, arquivo.read().split()))

end_of_inputs = False
index = 0

while not end_of_inputs:
    total_airports = data[index]
    total_empty_accents = data[index+1]
    athletes = data[index+2]
    index +=3
    
    Flights_trajectories = Flights(total_airports)
    
    for airport in range(1, total_airports+1):
        Flights_trajectories.add_adges((airport, 0), (airport, 1), athletes)
    
    for flight in range(total_empty_accents):
        origin_airport = data[index]
        destiny_airport = data[index+1]
        empty_accent = data[index+2]
        index+=3
        
        Flights_trajectories.add_adges((origin_airport, 0), (destiny_airport, 1), empty_accent)
        
    if (data[index] == 0) and (data[index] == 0) and (data[index] == 0):
        end_of_inputs = True
        
    end_of_the_trip = False
    day = 1
    while not end_of_the_trip:
        max_flow = Flights_trajectories.ford_fulkerson((1, 0),(total_airports, day),athletes)
        if max_flow >= athletes:
            print(day)
            break
        else:
            day += 1
            Flights_trajectories.expand_graph(day)
        
    
    
    
    
