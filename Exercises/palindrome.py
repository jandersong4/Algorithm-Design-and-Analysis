import math

string = "subi no onibus"
string = string.replace(" ", "")
string = string.lower()

n =  len(string)
is_palindrome = True
for i in range(math.floor(n/2)):
    print("{} -> {} || {} -> {}".format(i,string[i], (n-1-i), string[n-1-i]))
    if string[i] != string[n-1-i]:
        is_palindrome = False
print("Is palindrome -> {}".format(is_palindrome))