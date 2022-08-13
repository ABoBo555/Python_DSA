# to import file from another directory
import sys

sys.path.append("C:/Users/asus/Desktop/Python_DSA/single_linkedlist")

from single_linked_list import Linkedlist
from main import Cir_Linkedlist


def is_circular_linkedlist(ll):
    cur = ll.head
    while cur:
        if cur.next == ll.head:
            return True
        cur = cur.next
    return False


c_llist = Cir_Linkedlist()
c_llist.append(1)
c_llist.append(2)
c_llist.append(3)

s_llist = Linkedlist()
s_llist.append("A")
s_llist.append("B")
s_llist.append("C")

c_llist.print_list()
s_llist.print_list()
print(is_circular_linkedlist(c_llist))
print(is_circular_linkedlist(s_llist))
