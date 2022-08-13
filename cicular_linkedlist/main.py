# in cicular linkedlist head node is in last node's next thus it seems like a circle


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # print(self, self.data)


class Cir_Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        # if list is empty
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        # if nodes already in list
        cur = self.head
        while self.head != cur.next:
            cur = cur.next
        cur.next = new_node
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
        # print(count)
        return count

    def split_2list(self):
        length = self.len()
        mid = length // 2
        node = self.head
        count = 0
        prev = None
        while node and count < mid:
            count += 1
            prev = node
            node = node.next
        prev.next = self.head

        sec_part_llist = Linkedlist()
        while node.next != self.head:
            sec_part_llist.append(node.data)
            node = node.next
        sec_part_llist.append(node.data)

        self.print_list()
        print()
        sec_part_llist.print_list()


# Testing
# uncomment below codes and test
# llist = Linkedlist()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# llist.prepand("V")
# llist.prepand("P")

# # llist.remove("P")
# # llist.remove("B")
# # llist.remove("D")


# llist.print_list()

# print()
# print(llist.len())

# llist.split_2list()
