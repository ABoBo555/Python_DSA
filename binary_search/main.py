# Linear Search
def linear_search(arr, target):
    for i in range(len(arr) - 1):
        if arr[i] == target:
            return True
    return False


# Iterative Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


# Recursive Binary Search
def binary_search_recursive(arr, low, high, target):
    if low > high:
        return False
    mid = low + high // 2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return binary_search_recursive(arr, low, mid - 1, target)


def cloest_number_in_array(arr, target):
    min_diff = left_min_diff = right_min_diff = float("inf")
    low = 0
    high = len(arr) - 1
    cloest_num = None

    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return A[0]

    while low <= high:
        mid = (low + high) // 2

        # Ensure you do not read beyond the bounds
        # of the list.
        if mid + 1 < len(arr):
            right_min_diff = abs(arr[mid + 1] - target)
        if mid > 0:
            left_min_diff = abs(arr[mid - 1] - target)

        # Find the minimum difference between the target and
        # the current element.
        if left_min_diff < min_diff:
            min_diff = left_min_diff
            cloest_num = arr[mid - 1]

        if right_min_diff < min_diff:
            min_diff = right_min_diff
            cloest_num = arr[mid + 1]

        # Move the mid-point appropriately as is done
        # via binary search.
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
            if high < 0:
                return arr[mid]
        else:
            return arr[mid]
    return cloest_num


def find_fix_point_linear(arr):
    for i in range(len(arr) - 1):
        if arr[i] == i:
            return i
    return None


def find_fix_point_binary_search(arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            low = mid + 1
        else:
            high = mid - 1
    return None


# Sequence is called Bitonic if its in first increasing and then decreasing.
# arr[0] <= arr[1], arr[1] <= arr[2],…… & arr[i] >= arr[i+1], arr[i+1] >= arr[i+2]…… >= arr[n-1]
# 2, 3, 4, 7, 9, 8, 6, 5
def bitonic_peak(arr):
    low = 0
    high = len(arr) - 1

    if len(arr) < 3:
        return "Array should has at least lenght of 3, unless couldn't perform Bitonic."

    while low <= high:
        mid = (low + high) // 2

        left_mid = arr[mid - 1] if mid - 1 >= 0 else float("-inf")
        right_mid = arr[mid + 1] if mid + 1 < len(arr) else float("inf")

        if left_mid < arr[mid] and arr[mid] < right_mid:
            low = mid + 1
        elif left_mid > arr[mid] and arr[mid] > right_mid:
            high = mid - 1
        elif left_mid < arr[mid] and arr[mid] > right_mid:
            return arr[mid]
    return arr[low - 1]


def find_first_entry(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            if mid - 1 < 0:
                return mid
            if arr[mid - 1] != target:
                return mid
            high = mid - 1
    return None


def integer_square_root(k):
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        # print(mid)
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1


def smallest_num_in_cyc_shift_arr(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        elif arr[mid] <= arr[high]:
            high = mid
    return low


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 15
    # Linear Search & Binary Search.
    print("Linear Search & Binary Search")
    print(linear_search(arr, target))
    print(binary_search(arr, target))
    print(binary_search_recursive(arr, 0, len(arr) - 1, target))

    # Finding the closest number of a target number in list.
    print("\nClosest Number")

    A1 = [1, 2, 4, 5, 6, 6, 8, 9]
    A2 = [4, 8, 12, 16, 20, 24, 28]

    print(cloest_number_in_array(A1, 11))
    print(cloest_number_in_array(A2, 6))
    print(cloest_number_in_array(A2, 10))
    print(cloest_number_in_array(A2, 14))
    print(cloest_number_in_array(A2, 18))
    print(cloest_number_in_array(A2, 22))

    # Find the number which position is equal to its value.
    print("\nFixed Point")

    # Fixed point is 3:
    A1 = [-10, -5, 0, 3, 7]

    # Fixed point is 0:
    A2 = [0, 2, 5, 8, 17]

    # No fixed point. Return "None":
    A3 = [-10, -5, 3, 4, 7, 9]
    print("Linear Approach")
    print(A1)
    print(find_fix_point_linear(A1))
    print(A2)
    print(find_fix_point_linear(A2))
    print(A3)
    print(find_fix_point_linear(A3))
    print("Binary Search Approach")
    print(A1)
    print(find_fix_point_binary_search(A1))
    print(A2)
    print(find_fix_point_binary_search(A2))
    print(A3)
    print(find_fix_point_binary_search(A3))

    # Peak element is "5".
    print("\nBitonic peak!")
    A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print(bitonic_peak(A))
    A = [0, 1, 5, 4, 3, 2, 1]
    print(bitonic_peak(A))
    A = [1, 2, 3, 4, 5]
    print(bitonic_peak(A))
    A = [5, 4, 3, 2, 1]
    print(bitonic_peak(A))

    # First entry number in list with duplicates
    print("\nFirst entry number position!")
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    target = 108
    x = find_first_entry(A, target)
    print(x)

    # integer square root using divide and conquer
    print("\nInteger square!")
    print(integer_square_root(300))

    # Index of smallest number in cyclically shifted array
    print("\n Smallest number in Cyclically shifted array!")
    A = [4, 5, 6, 7, 1, 2, 3]
    idx = smallest_num_in_cyc_shift_arr(A)
    print(A[idx])
