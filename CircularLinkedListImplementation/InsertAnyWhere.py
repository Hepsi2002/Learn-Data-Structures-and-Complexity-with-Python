class _Node:
    __slots__ = '_element','_next'
    def __init__(self,element,next):
        self._element = element
        self._next = next

class CircularLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self,e):
        newest = _Node(e,None)
        if self.isempty():
            newest._next = newest
            self._head = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def insert_begin(self,e):
        newest = _Node(e,None)
        if self.isempty():
            newest._next = newest
            self._head = newest
        else:
            self._tail._next = newest
            newest._next = self._head
        self._head = newest
        self._size += 1

    def insert(self,e,position):
        newest = _Node(e,None)
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next = newest
        self._size += 1

    def display(self):
        p = self._head
        i=0
        while i < len(self):
            print(p._element,end = "-->")
            p = p._next
            i = i + 1
        print()

c = CircularLinkedList()
c.addlast(2)
c.addlast(6)
c.addlast(20)
c.addlast(7)
c.addlast(5)
c.addlast(70)
c.insert_begin(23)
c.insert_begin(15)
c.display()
print('Size',len(c))
c.insert(10,4)
c.display()
print('Size',len(c)) 