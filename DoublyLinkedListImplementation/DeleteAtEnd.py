class _Node:
    __slots__ = '_element','_next','_prev'
    def __init__(self,element,next,prev):
        self._element = element
        self._next = next
        self._prev = prev

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self,e):
        newest = _Node(e,None,None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail
            self._tail = newest
        self._size += 1

    def insert_begin(self,e):
        newest = _Node(e,None,None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head._prev = newest
            self._head = newest
        self._size += 1

    def insert(self, e, position):
        newest = _Node(e, None, None)
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i = i + 1
        newest._next = p._next
        p._next._prev = newest
        p._next = newest
        newest._prev = p
        self._size += 1
    def delete_begin(self):
        if self.isempty():
            print('List is empty')
            return
        e = self._head._element
        self._head = self._head._next
        self._head._prev = None
        self._size -= 1
        if self.isempty():
            self._tail = None
        return e
    def delete_end(self):
        if self.isempty():
            print('List is empty')
            return
        e =self._tail._element
        self._tail = self._tail._prev
        self._tail._next = None
        self._size -= 1
        return e

    def display(self):
        p = self._head
        while p:
            print(p._element,end='<-->')
            p = p._next
        print()

    def displayrev(self):
        p = self._tail
        while p:
            print(p._element,end='<-->')
            p = p._prev
        print()

d = DoublyLinkedList()
d.addlast(2)
d.addlast(6)
d.addlast(8)
d.addlast(15)
d.addlast(23)
d.display()
del_end = d.delete_end()
print('Deleted last element',del_end)
d.display()
d.displayrev()
print('Size:',len(d))


