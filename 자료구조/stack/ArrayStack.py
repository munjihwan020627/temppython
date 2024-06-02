
class Stack:

    def __init__(self,capacity = 100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def isEmpty(self):
        if self.top  == -1:
            return True
        else: return False

    def isFull(self):
        if self.top == self.capacity - 1:
            return True
        else: return False


    def push(self,e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]

    def display(self):
        for i in range(self.top, -1, -1):
            print(self.array[i], end=' ')
        print()
    def sortedPush(self, e):
        if (self.isEmpty() or e > self.peek()) and not self.isFull():
            self.push(e)
        else:
            temp = self.pop()
            self.sortedPush(e)
            self.push(temp)

    def pushbottom(self, e):
        if self.isEmpty():
            self.push(e)
        else:
            temp = self.pop()
            self.pushbottom(e)
            self.push(temp)

# 재귀 함수 내부의 if 문에는 재귀 호출 뿐만 아니라 다른 코드들도 함께 포함될 수 있으며, 해당 코드들은 재귀 함수가 반복된 횟수만큼 실행됨.




if __name__ == "__main__":
    Stack1 = Stack()
    Stack1.sortedPush(10)
    Stack1.sortedPush(70)
    Stack1.sortedPush(60)
    Stack1.sortedPush(50)
    Stack1.sortedPush(20)
    Stack1.sortedPush(40)
    Stack1.display()
    print(Stack1.peek())
    print(Stack1.pop())
    Stack1.display()