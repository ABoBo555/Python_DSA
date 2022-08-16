# What is Arrary Advanced Game?
# check => https://www.youtube.com/watch?v=r7EzxgrYfNg&list=PL5tcWHG-UPH1YSW2RraQg2L2p5hQTIpNL


def array_advance(arr):
    furthurest_reach = 0
    i = 0
    last_index = len(arr) - 1
    while i <= furthurest_reach and furthurest_reach < last_index:
        furthurest_reach = max(furthurest_reach, arr[i] + i)
        i += 1
    return furthurest_reach >= last_index


# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

# False: Not possible to navigate to last index in A:
A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))


arr1 = [1, 2, 3]
arr2 = [5, 6]
res = add(arr1, arr2)
print(res)
