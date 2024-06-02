class DListNode:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class DListType:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def addFront(self, data):
        node = DListNode(data,None, self.front) # 기존에 있던 맨 왼쪽의 노드가 곧 self.front이기에 그 앞에 넣으려면 self.front가 넣으려는 node의 next가 되어야함
        if self.size == 0:
            self.front = self.rear = node

        else:
            self.front.prev = node #기존에 있던 첫번째의 노드의 왼쪽이 노드임
            self.front = node
        self.size += 1

    def addPos(self,pos, data):
        node = DListNode(data, None, None)

        if pos == 1:
            self.addFront(data)
        elif pos == self.size + 1:
            self.addrear(data)
        elif pos> self.size+1:
            print("ERROR!")
        else:
            p = self.front

            """
            <뒤에서 pos을 맞출때>
            for _ in range(pos-1):
                p = p.next

            node.prev = p.prev
            node.next = p
            p.prev.next = node
            p.prev = node
            """
            # <앞에서 pos를 맞출때>
            for _ in range(pos-2):
                p = p.next

            node.prev = p
            node.next = p.next
            p.next = node
            p = node
            self.size += 1
            
            
            
    def addrear(self, data):
        node = DListNode(data, self.rear,None)
        if self.size == 0:
            self.front = self.rear = node

        else:
            self.rear.next = node
            self.rear = node
        self.size += 1




    def deleteFront(self):
        if self.size != 0:
            p = self.front
            data = p.data

            self.front = p.next

            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None

            self.size -= 1
            return data

    def deleterear(self):
        if self.size != 0:
            p = self.rear
            data = p.data

            self.rear = p.prev

            if self.rear == None:
                self.front = None

            else:
                self.rear.next = None

            self.size -= 1
            return data

    def display(self):
        p = self.front

        while p != None:
            print("[%c] <-> " %p.data, end= "")
            p = p.next
        print('\b\b\b\b   ')


if __name__ == "__main__":

    DL = DListType()
    DL.addFront('A'); DL.addFront('B');
    DL.addrear('C');  DL.addrear('D')
    DL.addPos(2,"E")
    DL.addPos(1,"F")
    DL.addPos(7,"G")


    print('[%c] is deleted' %DL.deleteFront(),end= "")
    print()
    print('[%c] is deleted' %DL.deleterear(),end= "")
    print()

    DL.display()