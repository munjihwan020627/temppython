class ArraySet:

    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.set = [None] * self.capacity
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def contain(self, e):
        if e in self.set:
            return True
        else: return False
    def isFull(self):
        if self.size == self.capacity:
            return True
        else:
            return False

    def insert(self, e):
        if not self.isFull() and not self.contain(e):
            self.set[self.size] = e
            self.size += 1

    def display(self):
        for i in range(self.size):
            print(self.set[i], end=' ')
        print()


    def replace(self,pos, e):
        if 0 <= pos < self.size:
            self.array[pos] = e

        else: pass



    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else: return None

    def delete(self, e):
        if not self.isEmpty() and self.contain(e):
            for i in range(self.size):
                if self.set[i] == e:
                    self.set[i] = self.set[self.size - 1]
                    self.size -= 1 #어짜피 if문 통과를 한번만 실행하니깐 어디서 size의 크기를 줄이든 상관 X
        else:
            print("UNDERFLOW OR INVALID POSITION")

    def union(self, setB):
        setC = ArraySet()

        for i in range(self.size):
            setC.insert(self.set[i])

        for i in range(setB.size):
            setC.insert(setB.set[i])

        return setC


    def intersection(self,setB):
        setC = ArraySet()
        for i in range(self.size):
            if setB.contain(self.set[i]):
                setC.insert(self.set[i])

        return setC

    def difference(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contain(self.set[i]):
                setC.insert(self.set[i])

        return setC

if __name__ == '__main__':
    S1 = ArraySet(50)
    S1.insert(100)
    S1.insert(200)
    S1.insert(300)
    S1.insert(400)
    S1.insert(20)
    S1.insert(30)
    S1.display()


    S2 = ArraySet()
    S2.insert(10)
    S2.insert(20)
    S2.insert(30)
    S2.insert(40)
    S2.display()

    S1.union(S2).display()
    S1.intersection(S2).display()

    S1.difference(S2).display()