class Set:

    def __init__(self, capacity=100):

        self.capacity = capacity
        self.set = [None] * self.capacity
        self.size = 0

    def isNone(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def contain(self, e):
        if e in self.set:
            return True
        return False

    """ 
    연습하면서 내가 작성한 부분   
    def contain(self,e):
        for i in range(self.size):
            if self.set[i] == e:
                return i
        return -1
    """

    def insert(self, e):
        if not self.isFull() and not self.contain(e):
            self.set[self.size] = e
            self.size += 1


    def delete(self, e):
        if not self.isNone() and self.contain(e):
            for i in range(self.size):
                if self.set[i] == e:
                    self.set[i] = self.set[self.size - 1]
                    self.size -= 1 #어짜피 if문 통과를 한번만 실행하니깐 어디서 size의 크기를 줄이든 상관 X
        else:
            print("UNDERFLOW OR INVALID POSITION")

    """
    내가 연습하면서 작성한 코드
    
     def delete(self, e):
        if not self.isNone() and self.contain(e):
            temp = self.contain(e)
            self.set[temp] = None
            for i in range(temp,self.size):
                self.set[i] = self.set[i+1]

            self.size -= 1
    """
    def display(self):
        for i in range(self.size):
            print(self.set[i], end=' ')
        print()



    """
        for i in range(self.size):
                if self.set[i] == e:
                    self.set[i] = self.set[self.size - 1]
                    self.size -= 1 #어짜피 if문 통과를 한번만 실행하니깐 어디서 size의 크기를 줄이든 상관 X
        
    """


    def union(self, SetB):
        SetC = Set()

        for i in range(self.size):
            SetC.insert(self.set[i])

        for i in range(SetB.size):
            SetC.insert(SetB.set[i])

        return SetC

    def intersection(self, SetB):
        SetC = Set()

        for i in range(self.size):
            if SetB.contain(self.set[i]):
                SetC.insert(self.set[i])

        return SetC

    def difference(self,SetB):
        SetC = Set()

        for i in range(self.size):
            if not SetB.contain(self.set[i]):
                SetC.insert(self.set[i])

        return SetC




"""

다른 set을 생성해서 거기에서 연산을 하는 경우 클래스를 불러와 준 뒤에
기존의 self에서 사용하던 set값들을 하나하나 다 입력해주고 그 이후에 사용해야함
self.set에 직접 접근 불가!!!!!


<정답>


SetC = Set()

for i in range(self.size):
    setC.insert(i) 




--------------------------------------->

<오답>
Set C = self.set 불가

"""




if __name__ == '__main__':
    S1 = Set(50)
    S1.insert(100)
    S1.insert(200)
    S1.insert(300)
    S1.insert(400)
    S1.insert(20)
    S1.insert(30)
    S1.display()


    S2 = Set()
    S2.insert(10)
    S2.insert(20)
    S2.insert(30)
    S2.insert(40)
    S2.display()

    S1.union(S2).display()
    S1.intersection(S2).display()

    S1.difference(S2).display()