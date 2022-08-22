def is_permutation_1(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    if len(s1) != len(s2):
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    if s1 == s2:
        return True
    else:
        return False


def is_permutation_2(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    if len(s1) != len(s2):
        return False

    ht = dict()
    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1

    return all(value == 0 for value in ht.values())


s1 = "google"
s2 = "ooggle"

s3 = "not"
s4 = "top"
print(is_permutation_1(s1, s1))
print(is_permutation_1(s3, s4))

print(is_permutation_2(s1, s1))
print(is_permutation_2(s3, s4))
