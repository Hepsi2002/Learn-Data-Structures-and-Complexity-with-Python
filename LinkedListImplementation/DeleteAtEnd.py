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
        newest = _Node(e,None)#Object is created
        if self.isempty():
            self._head = newest#This points to the first node(Newest node)
        else:
            self._tail._next = newest#Link is created
        self._tail = newest#The newest element will have its tail none.
        self._size += 1#Sizeis incremented as new node is added
    #Time complexity is O(1) takes unit time to compute.

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

    def insert(self,e,position):
        newest = _Node(e,None)
        #p,i are used to traverse the list from head to tail.
        p = self._head
        i = 1
        while i < position-1:
        #we are traversing the lsit till the given position-1 where the new node has to be inserted.
            p = p._next#moves to the next node
            i = i+1
        newest._next = p._next#since we dont want to loose reference we will store the address of the p.next
        p._next = newest#newest node reference is stored in the p.next making a link without loosing the reference
        self._size += 1

    def delete_begin(self):
        if self.isempty():
            print('Empty List')
            return
        e = self._head._element#element present in first node.
        self._head = self._head._next#second node will be the head
        self._size -= 1
        if self.isempty():
            self._tail = None#When only single node is present and is deleted we then explicitly make the tail as none.
        return e
    def delete_end(self):#We cannot directly delete the tail. Since we cannot move backwards from tail using next reference
       if self.isempty():
            print('Empty List')
            return
       p = self._head
       i = 1
       while i < len(self) - 1:#last but one node to make it null so there will be no link to next node
           p = p._next
           i = i + 1
       self._tail = p#last but one node will be tail
       p = p._next#to the last node the p is incremented as we need the value that is deleted
       e = p._element#last node element
       self._tail._next = None#breaking the link and making the last but one node as none.
       self._size -= 1
       return e

    def search(self,key):
        p = self._head#To keep track of node & the linked list
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next#if element is not equal to key, p value will be moved
            index=index+1
        return -1#when key is not found

    def display(self):
        p=self._head
        while p:#we can use for loop but we have used while loop as we need size.
            print(p._element,end='-->')
            p = p._next#For the last node the value of p will be none so the loop will terminate
        print()
    #Time complexity of the display method will be O(N).

L = LinkedList()
L.addlast(2)
L.addlast(6)
L.addlast(12)
L.addlast(12)
L.addlast(8)
L.addlast(7)
L.addlast(48)
L.addlast(9)
L.display()
print("Size of the list",len(L))
del_lastelement = L.delete_end()
print("Deleted Last Element",del_lastelement)
L.display()
print("Size of the list",len(L))


