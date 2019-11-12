class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def inorder(temp):
    if temp is None:
        return
    inorder(temp.left)
    print(temp.val, end=" ")
    inorder(temp.right)


root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

inorder(root)
