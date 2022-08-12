def JosephusProblem(n, k):
    if n == 1:
        return 1
    else:
        return (JosephusProblem(n - 1, k) + k - 1) % n + 1


print("JosephusProblem(3,2) = ", end=" ")
print(JosephusProblem(3, 2))
print("JosephusProblem(7,100) = ", end=" ")
print(JosephusProblem(7, 100))
