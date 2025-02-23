from listnode import ListNode

class ListType:

    def __init__(self):
        self.head = None
        self.size = 0


    def isNone(self):

        return self.head == None


    def insertFirst(self, data):

        node = ListNode(data, self.head)
        self.head = node
        self.size += 1


    def display(self):
        p = self.head

        while p != None:
            print('[%s] --> ' % p.data, end = "")
            p = p.next

        print('\b\b\b\b')

    def getNode(self, pos):
        p = self.head

        for i in range(1, pos - 1):
            p = p.next

        return p


    def insert(self, pos, data):
        if pos == 1:
            self.insertFirst(data)
        else:
            if(pos <= self.size + 1):
                p = self.getNode(pos)

                node = ListNode(data, p.next)
                p.next = node
                self.size += 1

            else:
                print("오류")

    def deleteFirst(self):
        if not self.isNone():
            p = self.head

            self.head = p.next
            self.size -= 1
            return p.data

    """
ANSWER
    def deleteFirst(self):
        if self.isNone():
            print("ERROR!")
        else:
            p = self.head
            
            self.head = p.next
            self.size -= 1
            return p.data
    """

    def delete(self, pos):
        if pos == 1:
            self.deleteFirst()
        else:
            if(pos <= self.size + 1):
                p = self.getNode(pos-1)
                q = self.getNode(pos)
                p.next = q.next
                self.size -= 1
                return q.data


    """
ANSWER    

    def delete(self, pos):
        if self.isNone():
            print("ERROR")
            return 
        if pos == 1:
            self.deleteFirst()
        else:
            if (pos<= self.size):
                q = self.getNode(pos)
                p = self.getNode(pos+1)
                q.next = p.next
                self.size -= 1
                return p.data
    """
    
    
    
if __name__ == "__main__":

    L = ListType()
    L.insertFirst('A')
    L.insertFirst('B')
    L.insert(2, "C")
    L.insert(1, "D")
    L.insert(5, "E")
    L.display()

    print()
    print("[%s] is deleted" % L.deleteFirst())

    L.deleteFirst()
    print("[%s] is deleted" % L.delete(3))
    L.display()