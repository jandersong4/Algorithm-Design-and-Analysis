sequence = [3,5,8,9,7,10]
n = len(sequence)
i = 1

while (i < n) and (sequence[i] > sequence[i-1]):
    i+=1
print("O item {} é menor que seu antecessor {}".format(sequence[i], sequence[i-1]))  