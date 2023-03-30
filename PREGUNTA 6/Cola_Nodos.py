
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
    
    def enqueue(self, e):
        newNode = SNode(e)
        if self.isEmpty():
            self._head = newNode

        else:
            self._tail.next = newNode

        self._tail = newNode
        self.len += 1

    def dequeue(self):
        res = None
        if not self.isEmpty():
            res = self._head.elem
            self._head = self._head.next
            if self._head is None:
                self._tail = None
            self.len -= 1
        else:
            print("Cola vacia!!!")
        return res
    
    def isEmpty(self):
        return self._head is None

    def __len__(self):
        return self.len

    def __str__(self):

        result = ""
        while not self.isEmpty():
            result += f"{self._head.elem}, "
            self._head = self._head.next
            self.len -= 1
        return result
