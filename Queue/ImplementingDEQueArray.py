class DEQueArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def addfirst(self,e):
        self._data.insert(0,e)#insert is a built-in method which inserts element at specified position

    def addlast(self,e):
        self._data.append(e)

    def removefirst(self):
        if self.isempty():
            print('DEQue is Empty')
            return
        return self._data.pop(0)

    def removelast(self):
        if self.isempty():
            print('DEQue is Empty')
            return
        return self._data.pop()

    def first(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._data[0]

    def last(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._data[-1]

d = DEQueArray()
d.addfirst(8)
d.addfirst(15)
d.addlast(12)
d.addlast(21)
print(d._data)
print('Length:',len(d))
print(d.removefirst())
print(d.removelast())
print('First Element',d.first())
print('Last Element',d.last())