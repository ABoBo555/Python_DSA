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


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 15
    print(linear_search(arr, target))
    print(binary_search(arr, target))
    print(binary_search_recursive(arr, 0, len(arr) - 1, target))

    A1 = [1, 2, 4, 5, 6, 6, 8, 9]
    A2 = [4, 8, 12, 16, 20, 24, 28]

    print(cloest_number_in_array(A1, 11))
    print(cloest_number_in_array(A2, 6))
    print(cloest_number_in_array(A2, 10))
    print(cloest_number_in_array(A2, 14))
    print(cloest_number_in_array(A2, 18))
    print(cloest_number_in_array(A2, 22))

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
