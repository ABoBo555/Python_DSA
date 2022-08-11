from single_likend_list import Linkedlist

# llist.append(8)
# llist.append(7)
# llist.append(5)

# llist2.append(4)
# llist2.append(5)
# llist2.append(6)

# llist => 8(ones place) / 7(tens place) / 5(hundreds place)
# llist2 => 4(ones place) / 5(tens place) / 6(hundreds place)

#     5 7 8   3 6 9
#    +6 5 4     4 1
#     -----   -----
#   1 2 3 2   4 1 0


# this method can be applied only if len(llist1) == len(llist2)

# def sum_two_list_method2(self, llist2):
#     node_l1 = self.head
#     node_l2 = llist2.head
#     list_one = []
#     list_two = []

#     while node_l1 and node_l2:
#         list_one.append(str(node_l1.data))
#         list_two.append(str(node_l2.data))
#         node_l1 = node_l1.next
#         node_l2 = node_l2.next

#     list_one = list_one[::-1]
#     list_two = list_two[::-1]
#     value_one = "".join(list_one)
#     value_two = "".join(list_two)
#     result = int(value_one) + int(value_two)
#     return result


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


llist_1 = Linkedlist()
llist_1.append(8)
llist_1.append(7)
llist_1.append(5)

# llist => 8(ones place) / 7(tens place) / 5(hundreds place)
# llist2 => 4(ones place) / 5(tens place) / 6(hundreds place)

llist_2 = Linkedlist()
llist_2.append(2)
llist_2.append(5)
llist_2.append(6)

llist_1.reverse_llist_iterative()  # reverse both list to get in hundred,ten,one format
llist_2.reverse_llist_iterative()

print("This is reverse llist1: ", end=" ")
llist_1.print_list()

print()

print("This is reverse llist2: ", end=" ")
llist_2.print_list()

print()

print("This is sum of two llist: ", sum_two_list(llist_1, llist_2))  # calling sum fun
