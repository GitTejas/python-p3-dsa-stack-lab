# lib/stack.py

class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) >= self.limit:
            return False  # Instead of raising an exception, return False
        self.items.append(item)
        return True

    def pop(self):
        if self.isEmpty():
            return None  # Instead of raising an exception, return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None  # Instead of raising an exception, return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return self.size() - 1 - self.items.index(target)
        return -1
