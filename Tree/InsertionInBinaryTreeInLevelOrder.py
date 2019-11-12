class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def in_order(temp):
    if temp is None:
        return
    in_order(temp.left)
    print(temp.val, end=" ")
    in_order(temp.right)


def insert(temp, key):
    q = []
    q.append(temp)

    while len(q):
        temp = q[0]
        q.pop(0)

        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)


root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

in_order(root)
print()
insert(root, 12)

in_order(root)