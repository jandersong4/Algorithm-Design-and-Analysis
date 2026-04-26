# numbers = [3,7,16,20,20,20,33]
numbers = [3,7,16,20,33]

repeated = []
n = len(numbers)

i = 1
while i < n:
    if numbers[i] == numbers[i-1]:
        repeated.append(numbers[i])
        while (i < n) and (numbers[i] == numbers[i-1]):
            i +=1
    i+=1
print(repeated)
            
