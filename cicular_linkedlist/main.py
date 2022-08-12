# in cicular linkedlist head node is in last node's next thus it seems like a circle


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        last_node = self.head
        while self.head != last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = self.head

    def prepand(self, data):
        new_node = Node(data)
        new_node.next = self.head
        cur_node = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while self.head != cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
        self.head = new_node

    def print_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end=" ")
            temp_node = temp_node.next
            if temp_node == self.head:
                break


llist = Linkedlist()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepand("V")

llist.print_list()
llist.print_list()
