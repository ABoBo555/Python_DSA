from stack import Stack


def reverse(text):
    temp_stack = Stack()
    reverse_str = ""
    for i in text:
        temp_stack.push(i)
    for j in range(len(temp_stack.items)):
        reverse_str += temp_stack.pop()
    return reverse_str


result = reverse(input("Enter text to reverse : "))
print("This is reverse string : ", result)
