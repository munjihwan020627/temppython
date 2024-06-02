class Stack:

    def __init__(self, capacity = 100):

        self.capacity = capacity
        self.top = 0
        self.stack = [None] * capacity


    def isNone(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


    def push(self, e):
        if not self.isFull():
            self.stack[self.top] = e
            self.size += 1

        else: pass

    def pop(self):
        if not self.isNone():
            temp = self.stack[self.top]
            self.top -= 1
            return temp

    def peek(self):
        if not self.isNone():
            return self.stack[self.top]

    def display(self):
        print(self.stack[self.top: -1])





class Set:

    def __init__(self, capapcity = 100):
        self.capacity = capapcity
        self.size = 0
        self.set = [None] * capapcity

    def contain(self, e):
        if e in self.set:
            return True
        return False


    def insert(self,e):
        if not self.contain(e):
            self.set[self.size] = e
        else:
            pass

    def delete(self, e):
        if self.contain(e):
            for i in range(self.size):
                if self.set[i] == e:
                    temp = i
                    self.set[temp] = None
            for i in range(temp, self.size-1):
                self.set[i] = self.set[i+1]
            self.size -= 1

    def minus(self, SetB):
        SetC = Set(100)
        for i in range(self.size):
            if not SetB.contain(i):
                SetC.insert(self.set[i])
        return SetC



    def plus(self, SetB):
        SetC = Set(100)
        for i in range(self.size):
            SetC.insert(self.set[i])
        for j in range(SetB.size):
            SetC.insert(SetB.set[j])
        return SetC

    def kyo(self, SetB):
        SetC = Set(100)
        for i in range(self.size):
            if SetB.contain(self.set[i]):
                SetC.insert(self.set[i])
        return SetC



class queue:
    def __init__(self,capacity = 100):
        self.capacity = capacity

        self.front = 0
        self.rear = 0
        self.queue = [None] * self.capacity



    def isNone(self):
        return self.front == self.rear


    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity


    def enqueue(self,e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = e


    def dequeue(self):
        if not self.isNone():
            self.front = (self.front + 1) % self.capacity

            return self.queue[self.front]


    def peek(self):
        if not self.isNone():
            return self.queue[(self.front + 1) % self.capacity]


    def display(self):

        for i in range((self.capacity + self.rear- self.front) % self.capacity):
            print(self.queue[(self.front + 1 + i) % self.capacity], end= " ")

        print()



class deque(queue):

    def __init__(self, capacity = 100):
        super().__init__()
        self.front = 0

    def addrear(self,e):
        self.enqueue(e)

    def addfront(self,e):
        if not self.isFull():
            self.queue[self.front] = e
            self.front = (self.front -1 + self.capacity) % self.capacity

    def deleterear(self):
        if not self.isNone():
            q = self.queue[self.rear]
            self.rear = (self.rear -1 + self.capacity) % self.capacity
            return q

    def deletefront(self):

        return self.dequeue()


    def getrear(self):
        if not self.isNone():
            return self.queue[self.rear]
    def getfront(self):
        if not self.isNone():
            return self.peek()



    def getmiddle(self):
        if ((self.rear - self.front + self.capacity) % self.capacity) % 2 == 1:
            temp = queue(100)

            for i in range(((self.rear - self.front + self.capacity) % self.capacity) // 2):
                temp.enqueue(self.queue[i])



def cnt(n):
    if n == 4:
        print("성공")
    else:
        print("실패")
        cnt(n+1)


if __name__ == "__main__":

    Q = queue(10)

    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    Q.enqueue(5)
    Q.display()

    print(Q.peek())
    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())

    Q.display()



    D = deque(10)

    D.addrear(1)
    D.addrear(2)
    D.addrear(3)
    D.addrear(4)
    D.addfront(1)
    D.addfront(2)
    D.addfront(3)
    D.addfront(4)

    D.display()


    print(D.deleterear())
    print(D.deleterear())
    print(D.deletefront())
    print(D.deletefront())

    D.display()

    print(D.getrear())
    print(D.getfront())


    cnt(1)
