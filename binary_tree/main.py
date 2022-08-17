class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_tree(object):
    def __init__(self, root):
        self.root = Node(root)

    def preorder(self, start, traversal):
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += str(start.value) + "-"
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += str(start.value) + "-"

        return traversal


tree = Binary_tree(1)
# print(
#     "This is tree obj :",tree,"\n",
#     "This is node obj :",tree.root,"\n",
#     "This is node_value :",tree.root.value)

# setup tree
# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7
# 4-5-2-6-7-3-1
#               1
#           /       \
#          2          3
#         /  \      /   \
#        4    5     6   7


tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.preorder(tree.root, ""))  # root-left-right
print(tree.inorder(tree.root, ""))  # left-root-right
print(tree.postorder(tree.root, ""))  # left-right-root
