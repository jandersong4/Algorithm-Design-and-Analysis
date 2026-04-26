list = [1,2,3,4,5,6,7,8,9]
subsets_list = [[2,3],[2,1],[5,6],[7,8],[6,3],[4,9]]

n = len(subsets_list)

for i in range(n):
    for j in range(i+1,n):
        disjoint = True
        for element_i in subsets_list[i]:
            for element_j in subsets_list[j]:
                if element_i == element_j:
                    disjoint = False
                    break
            if not disjoint:
                break
        if disjoint:
            print("Existe par disjunto:", i, j, subsets_list[i], subsets_list[j])
            found = True
            break 
    if found:
        break
    
if not found:
    print("Não existe par disjunto")

