def sqrtn(a, n):
    b = a
    while n > 1:
        b = b * a
        n = n - 1
    return b
print(sqrtn(5, 1000))