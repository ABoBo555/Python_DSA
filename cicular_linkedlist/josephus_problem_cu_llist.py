from main import Cir_Linkedlist

no_of_nodes = int(input("Enter the number of nodes : "))
step_size = int(input("Please Enter the step  size : "))

cu_llist = Cir_Linkedlist()

for i in range(1, no_of_nodes + 1):
    cu_llist.append(i)

print("This is circular_llist : ", end=" ")
cu_llist.print_list()
print()

cur = cu_llist.head
length = cu_llist.len()
count = 0
prev = None
while cur and length > 1:
    count += 1
    if count % step_size == 0:
        print("Deleted Node:", cur.data)
        prev.next = cur.next
        length -= 1
    prev = cur
    cur = cur.next
cu_llist.head = cur

print("This will be the last no: ", end=" ")
cu_llist.print_list()
