def int_to_str(input):

    if input < 0:
        input *= -1
        negative = True
    else:
        negative = False

    output = []

    if input == 0:
        output.append("0")
    else:
        while input > 0:
            output.append(chr(ord("0") + input % 10))
            input //= 10
            output = output[::-1]
    output = "".join(output)
    if negative:
        return "-" + output
    else:
        return output


input_int = 10
print(input_int)
print(type(input_int))

output_str = int_to_str(input_int)
print(output_str)
print(type(output_str))
