import sys

class Number_digits:
    def __init__(self,digit_a, digit_b):
        self.digit_a = digit_a
        self.digit_b = digit_b
        self.sum_counter = 0
        self.inverse_counter = 0
    
    def find_new_digit(self):        
        sum_a = sum(self.digit_a)
        sum_b = sum(self.digit_b)
        
        units = sum_b - sum_a
        max_element = max(self.digit_b[0], self.digit_b[-1])
        min_element = min(self.digit_b[0], self.digit_b[-1])
        
        while (self.digit_a[-1] < max_element) and units: 
            self.digit_a[-1]+=1
            self.sum_counter +=1
            units-=1
        if(self.digit_a[0] < min_element):
            self.inverse_counter+=1
            while units:
                self.digit_a[0]+=1
                self.sum_counter+=1
                units-=1
            self.digit_a.reverse()
        if(self.digit_a == self.digit_b):
            return self.sum_counter + self.inverse_counter
        else:
            self.inverse_counter+=1
        return self.sum_counter + self.inverse_counter

# nome_arquivo = sys.argv[1]

# with open(nome_arquivo, "r") as arquivo:
#     data = list(map(int, arquivo.read().split()))

data = sys.stdin.buffer.read().split()
    
tests_len = int(data[0])

test_index = 0  
index = 1

while test_index < tests_len:
    a = [int(digit) for digit in data[index].decode()]
    b = [int(digit) for digit in data[index + 1].decode()]
    number_digits = Number_digits(a,b)
    number_digits.digit_a = a
    number_digits.digit_b = b
    index+=2
    
    test_index += 1
    counter = number_digits.find_new_digit()
    print(counter)


