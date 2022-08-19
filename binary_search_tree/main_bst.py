import sys

sys.path.append("C:/Users/asus/Desktop/Python_DSA/binary_tree")
from main import Binary_tree


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, root, new_value):
        cur = root
        if cur.value < new_value:
            if cur.right:
                self.insert(cur.right, new_value)
            else:
                cur.right = Node(new_value)
        else:
            if cur.left:
                self.insert(cur.left, new_value)
            else:
                cur.left = Node(new_value)

    def search(self, root, value):
        cur = root
        if cur:
            if cur.value == value:
                return True
            elif cur.value < value:
                return self.search(cur.right, value)
            else:
                return self.search(cur.left, value)


def inorder(tree, start, traversal):
    if start:
        traversal = inorder(tree, start.left, traversal)
        traversal.append(start.value)
        traversal = inorder(tree, start.right, traversal)
    return traversal


def is_BST(tree):
    res = inorder(tree, tree.root, [])
    for i in range(1, len(res)):
        if res[i] < res[i - 1]:
            return False
    return True


# checking if the tree is a BST

# This is BST
bst = BST(10)
bst.insert(bst.root, 3)
bst.insert(bst.root, 1)
bst.insert(bst.root, 25)
bst.insert(bst.root, 9)
bst.insert(bst.root, 13)

# print(bst.search(bst.root, 9))
# print(bst.search(bst.root, 14))

# print(bst.inorder_bst(bst.root, []))
print(inorder(bst, bst.root, []))
print(is_BST(bst))


# This is not BST
tree = Binary_tree(15)
tree.root.left = Node(10)
tree.root.right = Node(20)
tree.root.left.left = Node(5)
tree.root.left.right = Node(13)
tree.root.right.left = Node(18)
tree.root.right.right = Node(7)
tree.root.left.left.left = Node(3)

print(is_BST(tree))
