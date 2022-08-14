class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        cur = self.head
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def prepend(self, data):
        node = Node(data)
        if not self.head:
            node.next = self.head
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def delete_node(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                if cur.prev is None:
                    self.head = cur.next
                    cur.next.prev = None
                    cur = None
                    return
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    cur = None
                    return
            cur = cur.next

    def insert_node_after(self, point, node):
        node = Node(node)
        cur = self.head
        if self.head is None:
            self.head = node
        else:
            while cur.data != point:
                cur = cur.next
            nxt_node = cur.next
            cur.next = node
            node.prev = cur
            node.next = nxt_node

    def insert_node_before(self, point, node):
        node = Node(node)
        cur = self.head
        prev = None
        if not self.head:
            self.head = node
        else:
            while cur.data != point:
                prev = cur
                cur = cur.next
            if cur == self.head:
                self.prepend(node.data)
            else:
                prev.next = node
                node.prev = prev
                node.next = cur
                cur.prev = node


# Testing

dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)

dllist.insert_node_before(5, 10)

dllist.insert_node_after(2, 11)

dllist.print_list()
