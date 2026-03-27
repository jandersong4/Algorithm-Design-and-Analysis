class Node():
    def __init__(self,data):
        self.data = data
        self.antecesor = None
        
class Stack():
    def __init__(self):
        self.top = None
        self.__size = 0
    
    def __len__(self):
        return self.__size
        
    def push(self, elem):
        newElement = Node(elem)
        pointer = self.top
        self.top = newElement
        self.top.antecesor = pointer
        self.__size += 1
        return
    
    def pop(self):
        if self.top == None:
            raise IndexError("Pilha vazia")
        else:
            pointer = self.top
            self.top = self.top.antecesor
            pointer.antecesor = None
            self.__size -=1
        return
    
    def __repr__(self):
        string = ""
        pointer = self.top
        while pointer:
            string += str(pointer.data) + "<-"
            pointer = pointer.antecesor
        return string
    
    def __str__(self):
        return self.__repr__()
    
    
stack = Stack()

stack.push(54)
stack.push(77)
stack.push(14)

print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)