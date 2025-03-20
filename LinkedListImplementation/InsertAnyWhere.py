'''This is a development of the previous demonstration not a new program.'''
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

    def search(self,key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index=index+1
    def insert_begin(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size +=1

    def insert(self,e,position):
        newest = _Node(e,None)
        p = self._head
        i = 1
        while i < position-1:
            p = p._next
            i = i+1
        newest._next = p._next
        p._next = newest
        self._size += 1

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
L.insert_begin(9)
L.insert_begin(5)
L.display()
L.insert(25,4)
L.insert(52,8)
L.display()
print("Size of the list",len(L))


