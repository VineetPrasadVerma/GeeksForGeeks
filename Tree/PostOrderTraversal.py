class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def post_order(temp):
    if temp is None:
        return
    post_order(temp.left)
    post_order(temp.right)
    print(temp.val, end=" ")


root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

post_order(root)
