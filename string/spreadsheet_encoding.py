# A = 1 , B = 2 , C = 3,..., Z = 26
#                 A  A
#                /    \
#         1*(26**1) + 1*(26**0)
# AA = 27 , AB = 28,...,ZZ = 702

# ord() return unicode point a string char
# print(ord("A")) #65
# print(ord("B")) #66
# print(ord("C")) #67


def encoding_capital(s):
    num = 0
    count = len(s) - 1
    for i in s:
        num += 26 ** count * (ord(i) - ord("A") + 1)
        count -= 1
    return num


print(encoding_capital("ZZ"))
