# in cicular linkedlist head node is in last node's next thus it seems like a circle


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # print(self, self.data)


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
            # print(temp_node.data, temp_node.next)
            print(temp_node.data, end=" ")
            temp_node = temp_node.next
            if temp_node == self.head:
                break

    def remove(self, key):
        head_node = self.head
        cur_node = self.head
        prev_node = None

        if key == self.head.data:
            if self.head == self.head.next:
                self.head = None
            else:
                while cur_node.next != self.head:
                    cur_node = cur_node.next
                cur_node.next = self.head.next
                self.head = cur_node.next
        else:
            while cur_node:
                if cur_node.data != key:
                    prev_node = cur_node
                    cur_node = cur_node.next
                else:
                    prev_node.next = cur_node.next
                    cur_node = None
                    break

    def len(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
            if node == self.head:
                break
        print(count)


llist = Linkedlist()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepand("V")
llist.prepand("P")

llist.remove("P")
llist.remove("B")
llist.remove("D")


llist.print_list()

print()
llist.len()
