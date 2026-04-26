import sys

file_name = sys.argv[1]

with open(file_name, "r", encoding="utf-8") as file:
    lines = [linha.strip() for linha in file]


# test_case_list = [lines[0]]
test_case_list = []

class Graph_input:
    def __init__(self, node_count, edge_count, edges_list):
        self.node_count = node_count
        self.edge_count = edge_count
        self.edge_list = edges_list


index = 1
while(index < 18):
    # print('index  inicial {}'.format(index))
    # aux_list = []
    # aux_list.append(lines[index])
    # aux_list.append(lines[index+1])
    node_count = lines[index]
    edge_count = lines[index+1]
    graph_input = Graph_input(node_count, edge_count, [])
    index = index + 2
    candidate = lines[index]
    # print(candidate)
    while len(candidate) > 1:
        # aux_list.append(candidate)
        graph_input.edge_list.append(candidate)
        # print(format('index: {} - candidate: {}'.format( index, candidate)))
        index +=1
        try:
            candidate = lines[index]
            # print(candidate)
        except:
            break
    # test_case_list.append(aux_list)
    test_case_list.append(graph_input)
    # print('index final {}'.format(index))
    # print('--------------------------')
                
# print(test_case_list[0].edge_list)
    
    
    

    

# adiciona ao array /
# adiciona no array /
# verifica o length do proximo array, se maior que 1 adiciona no mesmo arrat
# se = a 1 incrementa o array de arrays e começa um novo array