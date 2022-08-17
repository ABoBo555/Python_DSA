import sys

sys.path.append("C:/Users/asus/Desktop/Python_DSA/stack")

from stack import Stack


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1].value

    def __len__(self):
        return len(self.items)


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

    def level_order(self, start):
        que = Queue()
        que.enqueue(start)
        traversal = ""
        while len(que) > 0:
            traversal += str(que.peek()) + "-"
            node = que.dequeue()

            if node.left:
                que.enqueue(node.left)
            if node.right:
                que.enqueue(node.right)
        return traversal

    def reverse_level_order(self, start):
        que = Queue()
        stack = Stack()
        que.enqueue(start)
        while len(que) > 0:
            node = que.dequeue()
            stack.push(node.value)

            if node.right:
                que.enqueue(node.right)
            if node.left:
                que.enqueue(node.left)
        return stack


q = Queue()
q.enqueue(1)

tree = Binary_tree(1)


tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# print(tree.preorder(tree.root, ""))  # root-left-right
# print(tree.inorder(tree.root, ""))  # left-root-right
# print(tree.postorder(tree.root, ""))  # left-right-root

print(tree.level_order(tree.root))

res = tree.reverse_level_order(tree.root)
print(res.items[::-1])


# print(
#     "This is tree obj :",tree,"\n",
#     "This is node obj :",tree.root,"\n",
#     "This is node_value :",tree.root.value)

# setup tree
# 1-2-4-5-3-6-7- [preorder]=>root-left-right
# 4-2-5-1-6-3-7  [inorder] =>left-root-right
# 4-5-2-6-7-3-1  [postorder]=> left-right-root
#               1
#           /       \
#          2          3
#         /  \      /   \
#        4    5     6   7
