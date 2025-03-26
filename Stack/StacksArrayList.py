class StackArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def push(self,e):
        self._data.append(e)

    def pop(self):
        if self.isempty():
            print('Stack is empty')
        return self._data.pop()

    def top(self):
        if self.isempty():
            print('Stack is empty')
            return
        return self._data[-1]

s = StackArray()
s.push(1)
s.push(5)
s.push(12)
print(s._data)
print('Len',len(s))
print(s.top())
s.push(14)
print(s.pop())
print(s.isempty())
s.pop()
s.pop()
s.pop()
print(s.isempty())