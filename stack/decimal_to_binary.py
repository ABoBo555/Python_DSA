from stack import Stack


def to_binary(num):
    binary_stack = Stack()
    binary_code = ""
    while num > 0:
        binary_stack.push(str(num % 2))
        num = num // 2
    while not binary_stack.is_empty():
        binary_code += binary_stack.pop()

    return binary_code


print(to_binary(int(input("Enter decimal to covert binary code : "))))
# print(int(to_binary(56), 2) == 56)
