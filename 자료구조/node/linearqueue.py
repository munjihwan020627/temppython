
"""LINEARQUEUE"""



class ListNode:

    def __init__(self, data, next):

        self.data = data
        self.next = next

class linearqueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return (self.front == None) and (self.rear == None)

    def enqueue(self, data):
        node = ListNode(data, None)

        if self.isEmpty():
            self.rear = node
            self.front = node
            self.size += 1
        else:
            node.next = self.rear.next
            self.rear.next = node
            self.rear = node
            self.size += 1

    def dequeue(self):
        if not self.isEmpty():
            p = self.rear
            q = self.front
            data = q.data
            if p == q:
                self.rear = None
                self.front = None
            else:
                self.front = self.front.next

            self.size -= 1
            return data
        else:
            print("No Elements")

    def display(self):
        if self.isEmpty():
            print("NO ELEMENT")
            return

        p = self.front
        for i in range(self.size):
            print('[%s] -> ' %p.data , end= " ")
            p = p.next
        print('\b\b\b\b')

if __name__ == "__main__":

    Q = linearqueue()

    Q.enqueue('A'); Q.display()
    Q.enqueue('B'); Q.display()
    Q.enqueue('C'); Q.display()
    Q.enqueue('D'); Q.display()

    print('[%s] is deleted' % Q.dequeue())
    print('[%s] is deleted' % Q.dequeue())
    print('[%s] is deleted' % Q.dequeue())
    print('[%s] is deleted' % Q.dequeue())

    Q.enqueue('E'); Q.display()
    Q.enqueue('F'); Q.display()
    Q.enqueue('G'); Q.display()
    Q.enqueue('H'); Q.display()
    Q.enqueue('I'); Q.display()

    print('[%s] is deleted' % Q.dequeue())
    print('[%s] is deleted' % Q.dequeue())










