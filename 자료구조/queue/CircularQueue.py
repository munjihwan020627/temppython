#queueing theroy

class CircularQueue:

    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        if self.front  == self.rear:
            return True
        else: return False

    def isFull(self):
        if self.front == (self.rear + 1) % self.capacity:        #front의 위치를 비워서 사용하다가 원형 큐를 돌다가 front가 none이 아닌 곳에 마주쳤을때를 의미함
            return True
        else: return False


    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = e

        else: pass




    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.queue[self.front]
        else:
            pass

    def peek(self):
        if not self.isEmpty():
            return self.queue[(self.front + 1) % self.capacity]
    def display(self):
        print("Front: %d , Rear: %d" % (self.front, self.rear))
        i = self.front

        while i != self.rear:
            i = (i + 1) % self.capacity
            print('[%c]' % self.queue[i],end=" ")

        print()


    def display2(self):
        print(self.queue[self.front + 1 : self.rear + 1])





if __name__== "__main__":
    Q = CircularQueue()
    Q.enqueue('A')
    Q.enqueue('B')
    Q.enqueue('D')
    Q.enqueue('C')
    Q.enqueue('E')
    Q.enqueue('F')
    Q.display()
    print()
    print('Dequeue ---> ' ,Q.dequeue())
    print('peek -->', Q.peek())
    Q.enqueue('X')
    Q.enqueue('Y')
    Q.enqueue('Z')
    Q.enqueue('Q')
    Q.enqueue('W')
    Q.enqueue('T')
    Q.display()

""" 원형 queue의 경우 front의 위치를 (front + 1) % capacity를 통해 인덱스의 위치를 지정함 """