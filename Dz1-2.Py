a = float(input())
b = float(input())
c = input()
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
     print(a*b)
else:
    if (b == 0):
        print("невозможно")
    else:
        print(a/b)