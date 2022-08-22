import sys

# fibonancci with divide and conquer using recursion
def fib(num):
    if num < 2:  # optimal sol:
        return num
    return fib(num - 1) + fib(num - 2)


print(fib(7))
