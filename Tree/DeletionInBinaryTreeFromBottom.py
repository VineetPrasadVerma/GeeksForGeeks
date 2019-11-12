class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order(temp):
    if temp is None:
        return
    in_order(temp.left)
    print(temp.data, end=" ")
    in_order(temp.right)


def delete_deepest(root, delete_node):
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp is delete_node:
            temp = None
            return

        if temp.right:
            if temp.right == delete_node:
                temp.right = None
                return
            else:
                q.append(temp.right)

        if temp.left:
            if temp.left == delete_node:
                temp.left = None
                return
            else:
                q.append(temp.left)


def deletion(root, key):
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else:
            return root

    q = []
    q.append(root)
    deleted_node = None
    while len(q):
        temp = q.pop(0)
        if temp.data == key:
            deleted_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    if deleted_node:
        delete_deepest(root, temp)
    deleted_node.data = temp.data
    # temp = None
    return root

root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.left.right = Node(12)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)
print("The tree before the deletion:")
in_order(root)
key = 11
root = deletion(root, key)
print()
print("The tree after the deletion;")
in_order(root)
