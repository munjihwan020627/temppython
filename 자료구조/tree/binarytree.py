import queue




class TreeNode:
    def __init__(self, data, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None


    def PreOrder(self, node):
        if node is not None:
            print('[%c] ' %node.data, end="")
            self.PreOrder(node.left)
            self.PreOrder(node.right)



    def InOrder(self, node):
        if node is not None:
            self.PreOrder(node.left)
            print('[%c] ' %node.data, end="")
            self.PreOrder(node.right)



    def PostOrder(self, node):
        if node is not None:
            self.PreOrder(node.left)
            self.PreOrder(node.right)
            print('[%c] ' %node.data, end="")


    def LevelOrder(self, node):
        Q = queue.Queue()
        Q.put(node)

        while not Q.empty():
            node = Q.get()
            print('[%c] ' %node.data, end= '')

            if node.left != None:
                Q.put(node.left)

            if node.right != None:
                Q.put(node.right)




    def NodeCount(self, node):
        cnt = 0
        if node is not None:
            cnt = 1 + self.NodeCount(node.left) + self.NodeCount(node.right)

        return cnt

    def findexternal(self, node):
        if node.left is None and node.right is None:
            return True
        return False

    """
    <교수님 코드>
    def isExternal(self, node):
        return node.left == None and node.right == None
    
    """
    def LeafNodeCount(self, node):
        count = 0
        if node is not None:
            if self.findexternal(node):
                return 1
            else:
                count = self.LeafNodeCount(node.left) + self.LeafNodeCount(node.right)
        return count


    def getHeight(self, node):
        if node == None:
            return 0

        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1


if __name__ == "__main__":
    T = BinaryTree()

    n6 = TreeNode('F')
    n5 = TreeNode('E')
    n4 = TreeNode('D')
    n3 = TreeNode('C',n6)
    n2 = TreeNode('B',n4,n5)
    n1 = TreeNode('A',n2,n3)

    print('Pre : ', end=""); T.PreOrder(n1); print()
    print('In : ', end=""); T.InOrder(n1); print()
    print('Post : ', end=""); T.PostOrder(n1); print()
    print('Level : ', end=""); T.LevelOrder(n1); print()

    print("Node count : %d" %T.NodeCount(n1))
    print("Leaf count : %d" %T.LeafNodeCount(n1))
    print("get Height : %d" %T.getHeight(n1))
