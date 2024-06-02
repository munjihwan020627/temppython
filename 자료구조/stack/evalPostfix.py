from ArrayStack import Stack

def evalPostfix(expr):
    s = Stack(100)

    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if (token == "+"):
                s.push(val1 + val2)
            elif (token == "-"):
                s.push(val1 - val2)
            elif (token == "*"):
                s.push(val1 * val2)
            elif (token == "/"):
                s.push(val1 / val2)

        else:
            s.push(float(token))

    return s.pop()


if __name__ == '__main__':
    estr = '8 2 / 3 - 3 2 * +'
    expr = estr.split()
    print(expr, evalPostfix(expr))