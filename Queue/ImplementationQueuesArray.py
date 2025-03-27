class QueuesArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def enqueue(self,e):
        self._data.append(e)

    def dequeue(self):
        if self.isempty():
            print('Queue is empty')
            return
        else:
            return self._data.pop(0)

    def first(self):
        if self.isempty():
            print('Queue is empty')
            return
        return self._data[0]

q = QueuesArray()
q.enqueue(2)
q.enqueue(9)
print(q._data)
print('Length:',len(q))
q.enqueue(8)
q.enqueue(12)
print(q._data)
print(q.dequeue())
print(q._data)
print(q.first())
print(q._data)