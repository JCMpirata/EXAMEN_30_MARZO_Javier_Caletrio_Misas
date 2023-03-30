
class SNode:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

class Cola:
    def __init__(self):
        self._head = None
        self._tail = None
        self.len = 0

    def first(self):
        return self._head