vowels = "aeiou"

# Iterative length calculation: O(n)
def iterative_str_len(input_str):
    input_str_len = 0
    for i in range(len(input_str)):
        input_str_len += 1
    return input_str_len


# Recursive length calculation: O(n)
def recursive_str_len(input_str):
    if input_str == "":
        return 0
    return 1 + recursive_str_len(input_str[1:])


def iterative_count_consonants(input_str):
    consonant_count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowels and input_str[i].isalpha():
            consonant_count += 1
    return consonant_count


def recursive_count_consonants(input_str):
    if input_str == "":
        return 0

    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])


def recursive_multiply(x, y):
    if x < y:
        recursive_multiply(y, x)
    if y == 0:
        return 0
    return x + recursive_multiply(x, y - 1)


print("\nCount consonants!")
input_str = "abc de"
print(input_str)
print(iterative_count_consonants(input_str))
input_str = "LuCiDPrograMMiNG"
print(input_str)
print(recursive_count_consonants(input_str))

print("\nString Lenght!")
input_str = "LucidProgramming"

print(iterative_str_len(input_str))
print(recursive_str_len(input_str))


print(recursive_multiply(3, 6))
