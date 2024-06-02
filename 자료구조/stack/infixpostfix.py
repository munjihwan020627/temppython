from ArrayStack import Stack
from evalPostfix import evalPostfix
def precedence(op):
    if op in '()' :
        return 0
    elif op in '+-':
        return 1
    elif op in '*/':
        return 2
    else: return -1

def Infixpostfix(expr):
    s = Stack(100)

    output = []

    for token in expr:
        if token in "(":
            s.push('(')



        elif token in ')':
            while not s.isEmpty():
                op = s.pop()
                if op =='(':
                    break;
                else: output.append(op)

        elif token in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if( precedence(token) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break;
            s.push(token)

        else: output.append(token)

    while not s.isEmpty():
        output.append(s.pop())

    return output




if __name__ == "__main__":
    infix = input("Input infix expr :")
    expr = infix.split()
    postfix = Infixpostfix(expr)

    print(postfix , evalPostfix(Infixpostfix(postfix)))