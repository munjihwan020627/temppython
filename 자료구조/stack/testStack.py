class Stack:

    def __init__(self,capacity = 100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0


    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def push(self, e):
        if not self.isFull():
            self.array[self.size] = e
            self.size += 1


    def pop(self):
        if not self.isEmpty():
            self.size -= 1
            return self.array[self.size]
        #왜? -> size는 array 인덱스의 개수를 의미하기에 return할때는 size의 크기를 1 줄이고 pop해야 정상적으로 top에 있는 수가 pop됨


    def peek(self):
        if not self.isEmpty():
            return self.array[self.size]


    def display(self):
        for i in range(self.size-1, -1,-1):
            print(self.array[i], end = " ")



def checkBrackets(str):

    S = Stack(100)

    for c in str:
        if c in [ '[', '(', '{']:
            S.push(c)

        elif c in [ ']', ')', "}"]:
            if S.isEmpty():
                return False
            else:
                left = S.pop()
                if (c == ']' and left != '[' ) or (c == ')' and left != '(' ) or (c == '}' and left != '{' ):
                    return False
    return S.isEmpty()
"""
def checkBrackets(str):
    tempStack = Stack(100)

    for i in str:
        if i in ["[","{","("]:
            temp = i
            tempStack.push(temp)

        elif i in ["]","}",")"]:
            left = tempStack.pop()
            if (left == "[" and i== "]")or(left == "(" and i== ")")or(left == "{" and i== "}"):
                return True
            return False
    return tempStack.isEmpty()
    
    """

def evalPostfix(expr):
    S = Stack(100)
    for i in expr:
        if i in ["+","-","*","/"]:
            temp1 = S.pop()
            temp2 = S.pop()

            if i == "+":
                S.push(temp1 + temp2)
            elif i == "-":
                S.push(temp1 - temp2)
            elif i == "*":
                S.push(temp1 * temp2)
            elif i == "/":
                S.push(temp1 / temp2)


        else:
            S.push(float(i))

    return S.pop()

if __name__ == "__main__":

    s1 = "{asdfsadf}"
    s2 = "{asvdsadv]"
    s3 = "asvdsa}"
    s4 = " (sdvsadv"
    print(s1, checkBrackets(s1))
    print(s2, checkBrackets(s2))
    print(s3, checkBrackets(s3))
    print(s4, checkBrackets(s4))


    expr1 = ['13','12', '+','5','/']
    print(evalPostfix(expr1))