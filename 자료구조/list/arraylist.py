class ArrayList:

    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.size == self.capacity:
            return True
        else:
            return False

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:

            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            self.array[pos] = e
            self.size += 1
        else:
            print("OVERFLOW OR INVALID POSITION")

    def display(self):
        for i in range(self.size):
            print(self.array[i], end=' ')


    def replace(self,pos, e):
        if 0 <= pos < self.size:
            self.array[pos] = e

        else: pass



    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else: return None

    def delete(self, pos):
        if not self.isEmpty():
            e = self.array[pos]
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            return e
        else:
            print("UNDERFLOW OR INVALID POSITION")


if __name__ == '__main__':
    L1 = ArrayList(50)
    L1.insert(0,10)
    L1.insert(0,20)
    L1.insert(1,30)
    L1.display()





