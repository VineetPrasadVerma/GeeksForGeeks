def print_post_order(inorder, preorder, n):
    if preorder[0] in inorder:
        root = inorder.index(preorder[0])

    if root != 0:
        print_post_order(inorder[:root], preorder[1:root+1], len(inorder[:root]))

    if root != n-1:
        print_post_order(inorder[root+1:], preorder[root+1:], len(inorder[root+1:]))

    print(preorder[0], end=" ")


in_order = [4, 2, 5, 1, 3, 6]
pre_order = [1, 2, 4, 5, 3, 6]
n = len(in_order)
"Postorder traversal"
print_post_order(in_order, pre_order, n)