from ListType import ListType

S = ListType()

def push(data):
    S.insertFirst(data)

def pop():
    return S.deleteFirst()

def peek():
    if S.isNone():
        print("No result")
    else:
        p = S.head
        return p.data


push('A'); S.display()
push('B');S.display()

print('[%s] is deleted' %pop()); S.display()


