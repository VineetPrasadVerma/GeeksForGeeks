class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def in_order(root):
    if root is None:
        return "Empty Tree"
    else:
        s = []
        current = root

        while True:
            if current:
                s.append(current)
                current = current.left

            elif s:
                current = s.pop()
                print(current.val, end=" ")
                current = current.right

            else:
                break


root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

in_order(root)
