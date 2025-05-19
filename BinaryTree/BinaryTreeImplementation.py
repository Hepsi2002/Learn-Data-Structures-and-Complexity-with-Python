from QueuesLinkedList import QueueLinked
class _Node:
    __slots__ = '_element','_left','_right'

    def __init__(self,element,left=None,right=None):
        self._element = element
        self._left = left
        self._right = right

class BinaryTree:
    def __init__(self):
        self._root = None

    def maketree(self,e,left,right):
        self._root = _Node(e,left._root,right._root)#this statement will create a node for the binary tree, which is considered as the root of the binary tree or subtrees

    def inorder(self,troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element,end=' ')
            self.inorder(troot._right)

    def preorder(self,troot):
        if troot:
            print(troot._element, end=' ')
            self.preorder(troot._left)
            self.preorder(troot._right)

    def postorder(self,troot):
        if troot:
            self.postorder(troot._left)
            self.postorder(troot._right)
            print(troot._element, end=' ')

    def levelorder(self):
        '''Now in the level order traversal, we traverse level by level.
            So we need to store the references of the children of the nodes we visit in the level so that in the
            next level we can traverse them.We can achieve this with the help of queue'''
        q =QueueLinked()
        t = self._root
        print(t._element,end=' ')
        q.enqueue(t)
        while not q.isempty():
            t = q.dequeue()
            if t._left:
                print(t._left._element,end=' ')
                q.enqueue(t._left)
            if t._right:
                print(t._right._element,end=' ')
                q.enqueue(t._right)

    def count(self,troot):
        if troot:
            x = self.count(troot._left)
            y = self.count(troot._right)
            return x+y+1
        return 0

    def height(self,troot):
        if troot:
            x = self.height(troot._left)
            y = self.height(troot._right)
            if x>y:
                return x+1
            else:
                return y+1
        return 0
            


'''
#      10z
#   /       \
#  20x      30y

x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
a = BinaryTree()#This object will be used as a null binary tree for assigning left and right childs as null binary subtrees
x.maketree(20,a,a)#a-as there are no subtrees
y.maketree(30,a,a)
z.maketree(10,x,y)#x,y are given as they are the subtrees for nodes.
print('Inorder Traversal')
z.inorder(z._root)#As root node is indecated as z  we use the traversal methods using  z .
#_root is a variable which stores the reference of the root
print()
print('Preorder Traversal')
z.preorder(z._root)
print()
print('Postorder Traversal')
z.postorder(z._root)'''
#                 10t
#              /       \
#             20z      30s
#            /          /
#           40x        50r
#                       \
#                        60y

x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
a = BinaryTree()#This object will be used as a null binary tree for assigning left and right childs as null binary subtrees
x.maketree(40,a,a)#a-as there are no subtrees
y.maketree(60,a,a)
z.maketree(20,x,a)
r.maketree(50,a,y)
s.maketree(30,r,a)
t.maketree(10,z,s)#x,y are given as they are the subtrees for nodes.
print('Inorder Traversal')
t.inorder(t._root)#As root node is indecated as z  we use the traversal methods using  z .
#_root is a variable which stores the reference of the root
print()
print('Preorder Traversal')
t.preorder(t._root)
print()
print('Postorder Traversal')
t.postorder(t._root)
print()
print('Levelorder Traversal')
t.levelorder()
print()
print('No of Nodes')
print(t.count(t._root))
print('Height of the tree')
print(t.height(t._root))

