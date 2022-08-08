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
            # print(new_node)
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        # print(new_node)

    def print_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end=" ")
            temp_node = temp_node.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_new_node(self, prev_node, data):
        if not prev_node:
            print("Previous node doesn't exist.")
            return None

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_by_value(self, key):
        present_node = self.head

        if present_node and present_node.data == key:
            self.head = present_node.next
            present_node = None

        prev_node = None
        while present_node and present_node.data != key:
            prev_node = present_node
            present_node = present_node.next

        if present_node is None:
            return

        prev_node.next = present_node.next
        present_node = None

    def delete_by_position(self, pos):
        if self.head:
            present_node = self.head
            if pos == 0:
                self.head = present_node.next
                present_node = None

            prev_node = None
            count = 0
            while present_node and count != pos:
                prev_node = present_node
                present_node = present_node.next
                count += 1

            if present_node is None:
                return

            prev_node.next = present_node.next
            present_node = None

    def len_iterative_way(self):
        count = 0
        present_node = self.head
        while present_node:
            count += 1
            present_node = present_node.next
        return count

    def len_recursive_way(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive_way(node.next)


llist = Linkedlist()
llist.prepend("Head")
llist.append("A")
llist.append("B")
llist.append("C")


llist.insert_new_node(llist.head.next.next.next, "D")
# llist.insert_new_node(llist.head, "N") #insert after head node
# llist.insert_new_node(llist.head.next, "N") #insert after A node head.next is A object
# llist.insert_new_node(llist.head.next.next, "N") #insert after B node head.next.next is B object
# llist.insert_new_node(llist.head.next.next.next, "N") #insert after C node head.next.next.next is C object

llist.print_list()

llist.delete_by_value("D")
# llist.delete_by_position(0)

print()

llist.print_list()

print(
    "The length of the linked list calculated recursively after inserting 4 elements is:"
)
print(llist.len_recursive_way(llist.head))
print(
    "The length of the linked list calculated iteratively after inserting 4 elements is:"
)
print(llist.len_iterative_way())
