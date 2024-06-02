from ArrayStack import Stack

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

if __name__ == '__main__':
    s1 = "{asdfsadf}"
    s2 = "{asvdsadv]"
    s3 = "asvdsa}"
    s4 = " (sdvsadv"
    print(s1, checkBrackets(s1))
    print(s2, checkBrackets(s2))
    print(s3, checkBrackets(s3))
    print(s4, checkBrackets(s4))