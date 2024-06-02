class ListNode:

    def __init__(self, data, next):

        self.data = data
        self.next = next



class LinkedStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def isNone(self):

        return self.head == None

    def push(self, data):

        node = ListNode(data, self.head)
        self.head = node
        self.size += 1

    def display(self):
        p = self.head

        while p != None:
            print('[%s] --> ' % p.data, end="")
            p = p.next

        print('\b\b\b\b')

    def pop(self):
        if self.isNone():
            print("No result")
        else:
            p = self.head
            self.head = p.next
            self.size -= 1
            return p.data



    def peek(self):
        if self.isNone():
            print("No result")
        else:
            p = self.head
            return p.data


if __name__ == "__main__":

    S = LinkedStack()
    S.push('A'); S.display()
    S.push('B');S.display()
    S.push('D');S.display()
    S.push('F');S.display()
    S.push('C');S.display()
    S.peek()
    print('[%s] is deleted' %S.pop()); S.display()
    print('[%s] is deleted' %S.pop()); S.display()
    print('[%s] is deleted' %S.pop()); S.display()
    print('[%s] is deleted' %S.pop()); S.display()
    S.push('G'); S.display()


