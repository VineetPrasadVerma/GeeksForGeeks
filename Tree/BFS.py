class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def BFS(root):
    if root is None:
        print("Empty Tree")
    else:
        q =[]
        q.append(root)
        while len(q):
            temp = q.pop(0)
            if temp:
                print(temp.val, end=" ")
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)



root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)


BFS(root)
print()