class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def reverseBFS(root):
    if root is None:
        return

    s1 = []
    s2 = []
    s1.append(root)
    while s1:
        temp = s1.pop()
        s2.append(temp)
        if temp.left:
            s1.append(temp.left)
        if temp.right:
            s1.append(temp.right)
    while s2:
        temp = s2.pop()
        print(temp.data, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
reverseBFS(root)