TABLE_SIZE = 5

contacts = [
    ("Bob", 1234),
    ("Ikram", 5678),
    ("Pankaj", 9101),
    ("Peter", 2134),
    ("Jo", 1516),
    ("Maria", 1718),
]


def my_hash_function(key):
    return len(key) % TABLE_SIZE


def insert(contact, hash_table):
    if None not in hash_table:
        print("Hashtable is full")
        return

    index = my_hash_function(contact[0])

    print(f"Hash value of key is {index}")
    while hash_table[index] is not None:
        index += 1
        if index >= TABLE_SIZE:
            index = 0
    hash_table[index] = contact


def lookup(search_key, hash_table):
    index = my_hash_function(search_key)
    mark = index  # Keep track of where we start to avoid infinite loop
    while hash_table[index] and hash_table[index][0] != search_key:
        index += 1
        if index >= TABLE_SIZE:
            index = 0
        if index == mark:
            return f"{search_key} not included in list"
    if hash_table[index] is not None:
        return hash_table[index]


my_hash_table = [None] * TABLE_SIZE

for contact in contacts:
    insert(contact, my_hash_table)

print(my_hash_table)

print(lookup("LittleBob", my_hash_table))
