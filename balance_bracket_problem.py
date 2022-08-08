# Solving Balance Bracket problem using stack
# Examples of Balanced Brackets#
# { }
# { } { }
# (({[]}))
# Examples of Unbalanced Brackets#
# ( ( )
# { { { ) } ]
# [ ] [ ] ] ]
from stack import Stack


def is_pair(first, second):
    if first == ")" and second == "(":
        return True
    elif first == "]" and second == "[":
        return True
    elif first == "}" and second == "{":
        return True
    else:
        return False


def is_balance(brackets):
    stack = Stack()
    num_of_bracket = len(brackets)
    index = 0
    while num_of_bracket % 2 == 0:
        if brackets[index] in "({[":
            if index == num_of_bracket - 1:  # if only open brackets
                return False
            stack.push(brackets[index])
        else:
            if stack.is_empty():  # if only close brackets
                return False
            else:
                if not is_pair(brackets[index], stack.pop()):
                    return False

        if index == (num_of_bracket - 1) and stack.is_empty():
            return True

        index += 1

    else:
        return False


a = is_balance(input("Enter some bracket to check"))
print(a)
