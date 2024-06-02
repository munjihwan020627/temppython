import random

from CircularQueue import *

class CircularDeck(CircularQueue):

    def __init__(self,capacity = 10):
        super().__init__(capacity)

    def addFront(self, e):
        if not self.isFull():
            self.queue[self.front] = e
            self.front = (self.front -1 + self.capacity) % self.capacity
        else:  pass

    def addRear(self, e):

        self.enqueue(e)

    def deleteFront(self):

        self.dequeue()

    def deleteRear(self):
        if not self.isEmpty():
            self.rear = (self.rear - 1) % self.capacity
            return self.queue[self.rear]
        else: pass
    """
    정답코드
    def deleteRear(self):
        if not self.isempty():
            e = self.queue[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return e
        else: pass
    """
    def getFront(self):
        self.peek()

    def getRear(self):
        if not self.isEmpty():
            return self.queue[(self.rear) % self.capacity]


    """
    def getRear(self):
        if not self.isEmpty():
            return self.queue[self.rear]
    """


if __name__ == "__main__":
    D = CircularDeck()
    for i in range(4):
        D.addFront(random.randint(65,130))
    D.display()

    S = CircularDeck()
    for i in range(4):
        S.addRear(random.randint(65, 130))
    S.display()

    for i in range(2):
        D.deleteRear()
    D.display()

    for i in range(2):
        S.deleteRear()
    S.display()

