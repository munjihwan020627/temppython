class Node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = next

M = 13

class HashTable:
    def __init__(self):
        self.table = [None] * M

    def hashFn(self, key):
        return key % M

    def insert(self, key):
        b = self.hashFn(key)
        node = Node(key)
        node.next = self.table[b]
        self.table[b] = node

    def delete(self, key):
        b = self.hashFn(key)
        current = self.table[b]
        prev = None

        while current is not None:
            if current.data == key:
                if prev is None:
                    self.table[b] = current.next
                else:
                    prev.next = current.next
                return key
            current = current.next

    def search(self,key):
        b = self.hashFn(key)
        current = self.table[b]
        prev = None
        cnt = 0
        while current is not None:
            cnt +=1
            if current.data == key:
                return cnt
            current = current.next



    def display(self):
        for i in range(M):
            print("HT[%02d] : " %i, end="")
            n = self.table[i]
            if n == None:
                print()
            else:
                while n is not None:
                    print(n.data, end= " ")
                    n = n.next
                print()


if __name__ =="__main__":
    import random
    HT = HashTable()
    for i in range(30):
        HT.insert(random.randint(10,99))
    HT.insert(45)
    HT.display()

    print("45는 %d번째 배열의 %d번째에 있습니다!" %(HT.hashFn(45),HT.search(45)))
    print("%d가 삭제되었습니다" %HT.delete(45))

    HT.display()


    """
    이거 삭제나 검색연산 만들기 (과제는 아님)
    """