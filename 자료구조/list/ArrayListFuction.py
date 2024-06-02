capacity = 100
array = [None] * capacity
size = 0

def isEmpty():
    if size == 0:
        return True
    else: return False

def isFull():
    if size == capacity:
        return True
    else: return False


def insert(pos, e):
    global size
    if not isFull() and 0 <= pos <= size:

        for i in range(size, pos, -1):
            array[i] = array[i-1]
        array[pos] = e
        size += 1
    else:
        print("OVERFLOW OR INVALID POSITION")
    #if 7번인덱스까지 있는 리스트에서 8번째로 데이터값이 들어오려한다면? size를 증가시키면 됨
     #-> but 9번째로 들어오려면? Error 발생





def display():
    for i in range(size):
        print(array[i], end= ' ')


def delete(pos):
    global size
    if not isEmpty():
        e = array[pos]
        for i in range(pos, size - 1):
            array[i] = array[i + 1]
        size -= 1
        return e
    else:
        print("UNDERFLOW OR INVALID POSITION")



def findItem(e):
    for i in range(size):
        print(1)
        if array[i] == e:
            return i

        else:
            return  -1

if __name__ == "__main__":
    insert(0,1)
    insert(1,'B')
    insert(1,'C')
    insert(3, 'D')
    insert(4, 'E')

    display()



    e = input('Input item to delete: ')

    idx = findItem(e)
    if idx != -1:
        delete(idx)
    display()
    print(delete(1))
    display()
