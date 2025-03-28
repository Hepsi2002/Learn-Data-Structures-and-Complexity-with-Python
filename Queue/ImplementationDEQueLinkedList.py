'''This is a development of the previous demonstration not a new program. Time complexity for each function is given'''
class _Node:
    __slots__ = '_element','_next'
    def __init__(self,element,next):
        self._element = element
        self._next = next
#complexity analysis for the class _Node is O(1).

#This linked list class will have variables and methods to implement various operations that are performed on linked list.
class DEQueLinkedList:
    def __init__(self):
        self._front = None#head is an instance variable and will be accessed using self
        self._rear = None
        self._size = 0

    def __len__(self):#return no of elements in the list, it is a built-in class level method as len.
        return self._size
    def isempty(self):#this is our own defined method.Where as __init__ and __len__ are built-in class level functions.
        return self._size == 0 #True if size empty and false if size is not zero
    def addlast(self,e):#value of the element to be inserted.
        newest = _Node(e,None)#Object is created
        if self.isempty():
            self._front = newest#This points to the first node(Newest node)
        else:
            self._rear._next = newest#Link is created
        self._rear = newest#The newest element will have its tail none.
        self._size += 1#Sizeis incremented as new node is added
    #Time complexity is O(1) takes unit time to compute.

    def addfirst(self,e):
        newest = _Node(e,None)#New node is created
        if self.isempty():#if the node is the first node the head and tail will be the first node
            self._front = newest
            self._rear = newest
        else:
            newest._next = self._front#The head value is changed(newest node) since the element is added at the beginning of the node, the first node address will be stored in the newest node
            self._front = newest#The head will be the newest node
        self._size +=1#size will be incremented as new node is added
    #Time complexity of the insert_begin function will be O(1)



    def removefirst(self):
        if self.isempty():
            print('Empty List')
            return
        e = self._front._element#element present in first node.
        self._front = self._front._next#second node will be the head
        self._size -= 1
        if self.isempty():
            self._rear = None#When only single node is present and is deleted we then explicitly make the tail as none.
        return e
    #Time complexity is 0(1)

    def removelast(self):#We cannot directly delete the tail. Since we cannot move backwards from tail using next reference
       if self.isempty():
            print('Empty List')
            return
       p = self._front
       i = 1
       while i < len(self) - 1:#last but one node to make it null so there will be no link to next node
           p = p._next
           i = i + 1
       self._rear = p#last but one node will be tail
       p = p._next#to the last node the p is incremented as we need the value that is deleted
       e = p._element#last node element
       self._rear._next = None#breaking the link and making the last but one node as none.
       self._size -= 1
       return e
    #Time complexity of delete_end is O(N)

    def first(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._front._element

    def last(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._rear._element
    def search(self,key):
        p = self._front
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index=index+1
        return -1

    def display(self):
        p = self._front
        while p:
            print(p._element,end='-->')
            p = p._next
        print()


ql = DEQueLinkedList()
ql.addfirst(2)
ql.addfirst(6)
ql.addfirst(12)
ql.addlast(14)
ql.addlast(8)
ql.display()
print("Size of the list",len(ql))
print(ql.removefirst())
print(ql.removelast())
ql.display()
print('First Element:',ql.first())
print('Last Element:',ql.last())



