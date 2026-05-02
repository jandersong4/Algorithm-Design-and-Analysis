import sys
from collections import deque

MAX_VALUE = 10000

reverse_numbers = [0] * MAX_VALUE

for i in range(MAX_VALUE):
    reverse_numbers[i] = int(str(i)[::-1])

class Graph:
    def __init__(self):
        pass
        
    def invert_number(self, number):
        return reverse_numbers[number]

    def add_inverse_edge(self, u):
        return self.invert_number(u)
    
    def add_plus_one_edge(self, u):
        return u + 1
    
    def BFS(self, s, t):
        visited = [False] * MAX_VALUE
        distance = [0] * MAX_VALUE
        
        visited[s] = True
        
        queue = deque()
        queue.append(s)
        
        while queue:
            u = queue.popleft()
            
            if u == t:
                return distance[u]
            
            neighbors = [
                self.add_plus_one_edge(u),
                self.add_inverse_edge(u)
            ]
            
            for v in neighbors:
                if v < MAX_VALUE and not visited[v]:
                    visited[v] = True
                    distance[v] = distance[u] + 1
                    queue.append(v)
        
        return distance[t]


data = list(map(int, sys.stdin.buffer.read().split()))
    
tests_len = data[0]

index = 1
answers = []

for _ in range(tests_len):
    graph = Graph()

    a = data[index]
    b = data[index + 1]
    index += 2

    counter = graph.BFS(a, b)
    print(counter)