class List:




    def __init__(self,capacity = 100):

        self.capacity = capacity
        self.list = [None] * capacity
        self.size = 0

    def isNone(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


    def insert(self,pos,e):

        if not self.isFull() and 0<=pos<=self.size:
            for i in range(pos,self.size):
                self.list[i+1] = self.list[i]
            self.list[pos] = e
            self.size += 1


    def find(self,e):
        if not self.isNone() and e in self.list:
            for i in range(self.size):
                if self.list[i] == e:
                    return i


    def getEntry(self,pos):
        if 0<=pos<=self.size:
            return self.list[pos]

    def delete(self,pos):
        if not self.isNone() and 0<=pos<=self.size:
            self.list[pos] = None
            for i in range(pos,self.size-1):
                self.list[i] = self.list[i+1]
            self.size -= 1



    def whatislast(self):
        return self.list[self.size-1]





    def display(self):
        for i in range(self.size):

            print(self.list[i], end=" ")





if __name__ =="__main__":
    L1 = List()

    L1.insert(0,1)
    L1.insert(0, 2)
    L1.insert(1, 3)
    L1.delete(0)
    L1.display()
