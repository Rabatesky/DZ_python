a = int(input())
b = int(input())
if a < b:
    r = a
    a = b
    b = r
r = 1
while r != 0:
    while a >= b:
        a = a - b
    r = a
    a = b
    b = r
print(a)