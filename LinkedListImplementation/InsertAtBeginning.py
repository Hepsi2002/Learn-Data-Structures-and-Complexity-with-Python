class _Node:
    __slots__ = '_element','_next'
    def __init__(self,element,next):
        self._element = element
        self._next = next
#complexity analysis for the class _Node is O(1).

#This linked list class will have variables and methods to implement various operations that are performed on linked list.
class LinkedList:
    def __init__(self):
        self._head = None#head is an instance variable and will be accessed using self
        self._tail = None
        self._size = 0

    def __len__(self):#return no of elements in the list, it is a built-in class level method as len.
        return self._size
    def isempty(self):#this is our own defined method.Where as __init__ and __len__ are built-in class level functions.
        return self._size == 0 #True if size empty and false if size is not zero
    def addlast(self,e):#value of the element to be inserted.
        newest = _Node(e,None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def insert_begin(self,e):
        newest = _Node(e,None)#New node is created
        if self.isempty():#if the node is the first node the head and tail will be the first node
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head#The head value is changed(newest node) since the element is added at the beginning of the node, the first node address will be stored in the newest node
            self._head = newest#The head will be the newest node
        self._size +=1#size will be incremented as new node is added
    #Time complexity of the insert_begin function will be O(1)
    def search(self,key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index=index+1


    def display(self):
        p=self._head
        while p:
            print(p._element,end='-->')
            p = p._next
        print()


L = LinkedList()
L.addlast(2)
L.addlast(6)
L.addlast(12)
L.addlast(12)
L.addlast(8)
L.display()
print("Size of the list",len(L))
L.insert_begin(9)
L.display()
print("Size of the list",len(L))
L.insert_begin(5)
L.display()
print("Size of the list",len(L))


