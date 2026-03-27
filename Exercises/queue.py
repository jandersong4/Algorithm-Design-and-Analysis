class Node():
    def __init__(self,elem):
        self.data = elem
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0
        
    def __len__(self):
        return self.__size
    
    def __repr__(self):
        string = ""
        pointer = self.head
        while(pointer):
            string += str(pointer.data) + "->"
            pointer = pointer.next
        return string
            
    
    def __str__(self):
        return self.__repr__()

    def enqueue(self,elem):
        if self.head == None:
            self.head = Node(elem)
            self.tail = self.head
            self.__size+=1
        else:
            newElement = Node(elem)
            self.tail.next = newElement
            self.tail = newElement
            self.__size +=1
        return
    
    def dequeue(self):
        if self.head == None:
            raise IndexError("A fila está vazia")
        
        pointer = self.head
        self.head = pointer.next
        pointer.next = None
        if self.head == None:
            self.tail = None
            self.head = None
        self.__size -=1

queue = Queue()
queue.enqueue(38)
queue.enqueue(22)
queue.enqueue(33)
queue.enqueue(54)
print(queue)
queue.dequeue()
queue.dequeue()
print(queue)
