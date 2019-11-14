class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def pre_order(root):
    if root is None:
        return "Empty Tree"
    else:
        s = []
        current = root
        while True:
            if current:
                s.append(current)
                print(current.val, end=" ")
                current = current.left
            elif s:
                current = s.pop()
                current = current.right
            else:
                break


# root = Node(10)
# root.left = Node(11)
# root.left.left = Node(7)
# root.right = Node(9)
# root.right.left = Node(15)
# root.right.right = Node(8)

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

pre_order(root)