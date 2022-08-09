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
        print()

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

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return

        cur_1 = self.head
        prev_1 = None
        while cur_1 and key1 != cur_1.data:
            prev_1 = cur_1
            cur_1 = cur_1.next

        cur_2 = self.head
        prev_2 = None
        while cur_2 and key2 != cur_2.data:
            prev_2 = cur_2
            cur_2 = cur_2.next

        if not (cur_1 and cur_2):
            return

        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2

        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1

        cur_1.next, cur_2.next = cur_2.next, cur_1.next

    def reverse_llist_iterative(self):
        prev = None
        node = self.head
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        self.head = prev

    def reverse_llist_recursive(self):
        def _reverse_llist_recur(node, prev):
            present_node = node
            prev_node = prev
            if not present_node:
                return prev_node

            nxt = present_node.next
            present_node.next = prev_node
            prev_node = present_node
            present_node = nxt
            return _reverse_llist_recur(present_node, prev_node)

        self.head = _reverse_llist_recur(node=self.head, prev=None)

    def merge_two_sorted_llsit(self, llist2):
        p = self.head
        q = llist2.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next
        new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head

        return self.head


llist = Linkedlist()
llist.prepend("Head")
llist.append("A")
llist.append("B")
llist.append("C")

llist2 = Linkedlist()
llist2.prepend(1)
llist2.append(5)
llist2.append(7)
llist2.append(9)

llist3 = Linkedlist()
llist3.prepend(2)
llist3.append(4)
llist3.append(6)
llist3.append(8)

llist2.merge_two_sorted_llsit(llist3)
print("This is merging linkedlist 2&3 with merge_2sorted_llist_fun : ", end=" ")
llist2.print_list()


print("This is reversing the linkedlist by iterative : ", end=" ")
llist.reverse_llist_iterative()

llist.print_list()

print("This is re-reversing the linkedlist by recursive : ", end=" ")
llist.reverse_llist_recursive()

llist.print_list()

llist.insert_new_node(llist.head.next.next.next, "D")
# llist.insert_new_node(llist.head, "N") #insert after head node
# llist.insert_new_node(llist.head.next, "N") #insert after A node head.next is A object
# llist.insert_new_node(llist.head.next.next, "N") #insert after B node head.next.next is B object
# llist.insert_new_node(llist.head.next.next.next, "N") #insert after C node head.next.next.next is C object
print("This is inserting new node : ", end=" ")
llist.print_list()


llist.delete_by_value("D")
# # llist.delete_by_position(0)

# llist.print_list()

print(
    "The length of the linked list calculated recursively after inserting 4 elements is:",
    llist.len_recursive_way(llist.head),
)
print(
    "The length of the linked list calculated iteratively after inserting 4 elements is:",
    llist.len_iterative_way(),
)

print("Original list of before swapping : ", end=" ")
llist.print_list()

llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes : ", end=" ")
llist.print_list()

llist.swap_nodes("A", "B")
print("Swapping nodes A and B where key_1 is head node : ", end=" ")
llist.print_list()

llist.swap_nodes("A", "Head")
print("Swapping nodes A and Head where key_2 is head node : ", end=" ")
llist.print_list()

llist.swap_nodes("D", "B")
print("Swapping nodes D and B where D is not a node : ", end=" ")
llist.print_list()

llist.swap_nodes("C", "C")
print("Swapping nodes C and C where both keys are same : ", end=" ")
llist.print_list()
