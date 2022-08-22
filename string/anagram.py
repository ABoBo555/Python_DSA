def is_anagram(s1, s2):
    ## normalizing the strings
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    ht = dict()

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for j in s2:
        if j in ht:
            ht[j] -= 1
        else:
            ht[j] = 1

    for k in ht:
        if ht[k] != 0:
            return False
    return True


s1 = "fairy tales"
s2 = "rail safety"
print(is_anagram(s1, s2))
