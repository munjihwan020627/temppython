M = 13
table = [0] * M






def hashFn(key):
    return key % M


def hashFn2(key):
    return 11- (key % 11)


def getLinear(v, i):

    return (v + i) % M

def getQuardratic(v, i):
    return (v + i * i) % M



def getDouble(v, i, key):
    return (v + i * hashFn2(key)) % M




def insert(key):
    v = hashFn(key)
    i = 0  #해당 위치에서 이동한 횟수(자기자리로 갈필요는 없음)

    while i<M:
        b = getLinear(v, i)
        # b = getQuardratic(v, i)
        # b = getDouble(v, i, key)

        if table[b] == 0 or table[b] == 1:
            table[b] = key
            return
        else:
            i += 1





def search(key):
    v = hashFn(key)
    i = 0  #해당 위치에서 이동한 횟수(자기자리로 갈필요는 없음)

    while i<M:
        b = getLinear(v, i)
        # b = getQuardratic(v, i)
        # b = getDouble(v, i, key)

        print('[%d] ' % table[b])
        if table[b] == 0:
            return 0

        elif table[b] == key:
            return table[b]
        else:
            i += 1
    return 0






def delete(key):
    v = hashFn(key)
    i = 0  #해당 위치에서 이동한 횟수(자기자리로 갈필요는 없음)

    while i<M:
        b = getLinear(v, i)
        # b = getQuardratic(v, i)
        # b = getDouble(v, i, key)

        print('[%d] ' % table[b])
        if table[b] == 0:
            print("No Key to delete")
            return

        elif table[b] == key:
            table[b] = -1
            return
        else:
            i += 1
    return 0




def display():
    print()
    print('Bucket   key')
    print("============")
    for i in range(M):
        print('HT[%2d] :%2d' %(i, table[i]))



if __name__ == "__main__":
    data = [45, 27, 88, 9, 71, 60, 46, 38, 24]
    for d in data:
        print('h(%2d) = %2d' %(d,hashFn(d)), end="")
        insert(d)

        print(table)

    display()
    print()
    print('Search (46) --->',search(46))
    print('Search (39) --->',search(39))

    delete(60)
    display()

    print('Search (46) --->',search(46))