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

    def remove_duplicates(self):
        node = self.head
        prev = None
        dict_for_dup = dict()

        while node:
            if node.data in dict_for_dup:
                prev.next = node.next
                node = None
            else:
                dict_for_dup[node.data] = 1
                prev = node
            node = prev.next

    def nth_from_last_node(self, nth, method):
        if method == 1:
            llist_len = self.len_iterative_way()
            node = self.head
            while node and nth > 0 and nth <= llist_len:
                if llist_len == nth:
                    return node.data
                llist_len -= 1
                node = node.next
            else:
                return

        if method == 2:
            p = self.head
            q = self.head

            if nth > 0:
                count = 0
                while q:
                    count += 1
                    if count == nth:
                        break
                    q = q.next

                if not q:
                    return "The nth value is greater than the len of llist"

                while p and q.next:
                    p = p.next
                    q = q.next
                return p.data
            else:
                return

    def count_occurrence_of_one_node(self, nodedata):

        node = self.head
        count = 0
        while node:
            if node.data == nodedata:
                count += 1
            node = node.next
        return count

    def count_occurrence_of_one_node_recursive(self, node, nodedata):
        if node:
            if node.data == nodedata:
                return 1 + self.count_occurrence_of_one_node_recursive(
                    node.next, nodedata
                )
            else:
                return self.count_occurrence_of_one_node_recursive(node.next, nodedata)
        else:
            return 0

    def count_occurrence_of_all_node(self):
        node = self.head
        count = dict()
        while node:
            if node.data not in count:
                count[node.data] = 1
            else:
                count[node.data] += 1
            node = node.next
        return count

    def rotate(self, point):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            count = 0
            prev = None
            while p and count < point:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev

            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None

    def is_palindrome(self, method):
        if method == 1:
            node = self.head
            data_list = []
            while node:
                data_list.append(node.data)
                node = node.next
            return data_list == data_list[::-1]

        if method == 2:
            node = self.head
            data_list = []
            while node:
                data_list.append(node.data)
                node = node.next

            node = self.head
            while node:
                if node.data != data_list.pop():
                    return False
                node = node.next
            return True

        if method == 3:
            if self.head:
                node = self.head
                data_list = []
                i = 0
                while node:
                    data_list.append(node.data)
                    node = node.next
                    i += 1
                node = self.head
                count = 1
                while count <= (i // 2 + 1):
                    if data_list[-count] != node.data:
                        return False
                    node = node.next
                    count += 1
                return True
            else:
                return True

    def head_tail_swap(self):
        head_node = self.head
        node = self.head
        sec_prev = None

        while node and node.next:
            sec_prev = node
            node = node.next

        node.next = head_node.next
        head_node.next = None
        sec_prev.next = head_node
        self.head = node

    def move_tail_to_head(self):
        head_node = self.head
        node = self.head
        sec_prev = None

        while node and node.next:
            sec_prev = node
            node = node.next

        node.next = head_node
        sec_prev.next = None
        self.head = node


# Testing

llist = Linkedlist()
llist.prepend("H")
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("Y")
llist.append("Z")
llist.append("B")
llist.append("O")


llist.print_list()

llist.head_tail_swap()
print("This is head and tail swap : ", end=" ")
llist.print_list()

llist.move_tail_to_head()
print("This is moving tail-node to head : ", end=" ")
llist.print_list()


print("Is this llist palindrome : ", end="")
print(llist.is_palindrome(3))

print("This is count of all node : ", end=" ")
print(llist.count_occurrence_of_all_node())

print("This is count of 'A' node : ", end=" ")
print(llist.count_occurrence_of_one_node("A"))
# print(llist.count_occurrence_of_one_node_recursive(llist.head, "A"))

print("This 2th node from last : ", end=" ")
# print(llist.nth_from_last_node(3, 2))
print(llist.nth_from_last_node(2, 1))


llist.remove_duplicates()
print("This is removing duplicates from llist : ", end=" ")
llist.print_list()

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
print("This is inserting new node D : ", end=" ")
llist.print_list()


llist.delete_by_value("D")
print("This is delete by value D : ", end=" ")
llist.print_list()

llist.delete_by_position(5)
print("This is delete by position-5 'Y' :", end=" ")
llist.print_list()

print("Length of the linkedlist by recursively:", llist.len_recursive_way(llist.head))
print("Length of the linkedlist by iterative:", llist.len_iterative_way())

print("Original list of before swapping : ", end=" ")
llist.print_list()

llist.swap_nodes("B", "C")
print("Swapping nodes B and C  : ", end=" ")
llist.print_list()

llist.swap_nodes("Z", "A")
print("Swapping nodes Z and A  : ", end=" ")
llist.print_list()

llist.swap_nodes("H", "C")
print("Swapping nodes H and C where key_1 is head node : ", end=" ")
llist.print_list()

llist.swap_nodes("A", "B")
print("Swapping nodes A and B where key_1 is last node : ", end=" ")
llist.print_list()

llist.swap_nodes("C", "B")
print("Swapping nodes C and B where key_1-head,key_2-last node : ", end=" ")
llist.print_list()

llist.swap_nodes("C", "C")
print("Swapping nodes C and C where both keys are same : ", end=" ")
llist.print_list()

llist.rotate(3)
print("This is rotate a llist at point H : ", end=" ")
llist.print_list()


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
