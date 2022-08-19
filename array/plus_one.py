# list => 9 9 8
# plus 1 to the list=> 9 9 9
#                       +  1
#                 ------------
#                    1 0 0 0


def plus_one(list1):

    list1[-1] += 1

    for i in reversed(range(1, len(list1))):
        if list1[i] == 10:
            list1[i] = 0
            list1[i - 1] += 1
    if list1[0] == 10:
        list1[0] = 1
        list1.append(0)
    return list1


list1 = [9, 9, 9]
print(plus_one(list1))


def pair_of_sum(list1, target):

    for i in range(len(list1) - 1):
        for j in range(i + 1, len(list1)):
            if list1[i] + list1[j] == target:
                print(list1[i], list1[j])


pair_of_sum([10, 2, 3, 4, 9], 13)
