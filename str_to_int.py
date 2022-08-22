def str_to_int(input):

    output = 0

    if input[0] == "-":
        start_idx = 1
        negative = True
    else:
        negative = False
        start_idx = 0

    for i in range(start_idx, len(input)):
        place = 10 ** (len(input) - (i + 1))
        digit = ord(input[i]) - ord("0")
        output += place * digit

    if negative:
        return -1 * output
    else:
        return output


s = "554"
x = str_to_int(s)
print(type(x))

s = "123"
print(str_to_int(s), type(str_to_int(s)))

s = "-123"
print(str_to_int(s), type(str_to_int(s)))
