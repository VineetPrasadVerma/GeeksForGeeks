class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)
    if left > right:
        h = 1 + left
    else:
        h = 1 + right

    return h


root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

print(height(root))