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
            print(cur.data, end=" ")
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
        previous = None
        if not self.head:
            self.head = node
        else:
            while cur.data != point:
                previous = cur
                cur = cur.next
            if cur == self.head:
                self.prepend(node.data)
            else:
                previous.next = node
                node.prev = previous
                node.next = cur
                cur.prev = node

    def delete_node_by_value(self, value):
        cur = self.head
        previous = None
        while cur.data != value:
            previous = cur
            cur = cur.next
        if cur == self.head:
            self.head = self.head.next
        elif not cur.next:
            previous.next = None
        else:
            previous.next = cur.next
            cur.next.prev = previous

    def reverse_dllist(self):
        previous = None
        cur = self.head
        while cur:
            previous = cur
            cur.next, cur.prev = cur.prev, cur.next
            cur = cur.prev
        self.head = previous

    def remove_duplicates(self):
        cur = self.head
        previous = None
        duplicate = list()
        while cur:
            if cur.data in duplicate:
                previous.next = cur.next
                cur = cur.next
            else:
                duplicate.append(cur.data)
                previous = cur
                cur = cur.next

    def pairs_with_sum(self, sum):
        cur1 = self.head
        cur2 = self.head.next
        pair = []
        while cur1 and cur2:
            while cur2:
                if (cur1.data + cur2.data) == sum:
                    pair.append((cur1.data, cur2.data))
                cur2 = cur2.next
            cur1 = cur1.next
            cur2 = cur1.next
        print(pair)


# Testing

dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(5)
dllist.append(8)
dllist.append(4)
dllist.append(9)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(2)
dllist.append(1)
dllist.prepend(5)

# dllist.insert_node_before(5, 10)

# dllist.insert_node_after(2, 11)

# dllist.delete_node_by_value(2)

# dllist.reverse_dllist()
dllist.print_list()
print()

dllist.remove_duplicates()
dllist.print_list()
print()

dllist.pairs_with_sum(13)

dllist.print_list()
