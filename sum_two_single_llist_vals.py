# llist.append(8)
# llist.append(7)
# llist.append(5)

# llist2.append(4)
# llist2.append(5)
# llist2.append(6)

# llist => 8(ones place) / 7(tens place) / 5(hundreds place)
# llist2 => 4(ones place) / 5(tens place) / 6(hundreds place)

#     5 7 8
#    +6 5 4
#     -----
#   1 2 3 2


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
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next

    def reverse_llist_iterative(self):
        temp_node = self.head
        prev = None
        while temp_node:
            nxt = temp_node.next
            temp_node.next = prev
            prev = temp_node
            temp_node = nxt
        self.head = prev

    def sum_two_list_method2(self, llist2):
        node_l1 = self.head
        node_l2 = llist2.head
        list_one = []
        list_two = []

        while node_l1 and node_l2:
            list_one.append(str(node_l1.data))
            list_two.append(str(node_l2.data))
            node_l1 = node_l1.next
            node_l2 = node_l2.next

        list_one = list_one[::-1]
        list_two = list_two[::-1]
        value_one = "".join(list_one)
        value_two = "".join(list_two)
        result = int(value_one) + int(value_two)
        return result


def sum_two_list(list1, list2):
    node = list1.head
    list_one = []
    while node:
        list_one.append(str(node.data))
        node = node.next

    node = list2.head
    list_two = []
    while node:
        list_two.append(str(node.data))
        node = node.next

    # if len(llist)!=len(llist2) insert 0  @beginning of the lists
    while len(list_one) < len(list_two):
        list_one.insert(0, "0")

    while len(list_two) < len(list_one):
        list_two.insert(0, "0")

    value_one = "".join(list_one)
    value_two = "".join(list_two)
    result = int(value_one) + int(value_two)
    return result


llist = Linkedlist()
llist.append(8)
llist.append(7)
llist.append(5)

# llist => 8(ones place) / 7(tens place) / 5(hundreds place)
# llist2 => 4(ones place) / 5(tens place) / 6(hundreds place)

llist2 = Linkedlist()
llist2.append(4)
llist2.append(5)
llist2.append(6)

llist.reverse_llist_iterative()  # reverse both list to get in hundred,ten,one format
llist2.reverse_llist_iterative()

print("This is reverse llist1: ", end=" ")
llist.print_list()

print()

print("This is reverse llist2: ", end=" ")
llist2.print_list()

print()

print("This is sum of two llist: ", sum_two_list(llist, llist2))  # calling sum fun
