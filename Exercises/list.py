numbers = [1, 2, 3, 4, 5]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.__size = 0
        
    def append(self, elem):
        if self.head:
            #inserção quando a lista possui elemento
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
            self.__size+=1
        else:
            #primeira inserção
            self.head = Node(elem)
            self.__size+=1
            
    def __len__(self):
        #Retorna o tamanho da lista
        return self.__size
    
    def _getnode(self,index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer
    
    ##pq estamos usando o getitem desse jeito ?
    # Como funciona a sobrecaga de operador ?
    def __getitem__(self,index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")
    
    def __setitem__(self,index, elem):
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")
    
    def index(self, elem):
        #Retorna o indice do elemento na lista
        pointer = self.head
        i = 0 
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i+=1
        raise ValueError("{} is not in list".format(elem))
    
    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self.__size += 1
    
    def remove(self,elem):
        if self.head == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                     ancestor.next = pointer.next
                     pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            return True
        raise ValueError("{} is not in list".format(elem))
                
    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r
        
    
    def __str__(self):
        return self.__repr__()
        
        
        # index = self.index(elem)
        # node = self._getnode(index)
        # pointer = self.head
        # if index == 0:
        #     self.head = pointer.next
        #     return
        # else:
        #     for i in range(index):
        #         pointer.next = node.next
        #     if(pointer.next):
        #         pointer
            
    
list = LinkedList()

list.append(77)
list.append(45)
list.append(15)
list.insert(1,22)
list.remove(45)

print(list)
list.append(99)
print(list)
list.remove(22)
print(list)