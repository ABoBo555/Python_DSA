# 111221 is read off as "three 1s, two 2s, then one 1" or 312211.


def look_and_say(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])

        i += 1
    return "".join(result)


s = "1"
print(s)  # This is initial assignment of 1

n = 3
for i in range(n):
    s = look_and_say(s)
    print(s)
