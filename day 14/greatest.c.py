a = int(input("enter the number of a"))
b = int(input("enter the number of b"))
c = int(input("enter the number of c"))
if a >= b and a >= c:
    print(f" c is the greatest number {c}")
elif b >= a and b >= c:
    print(f" b is the greatest number{b}")
else:
    print(f" a is the greatest number {a}")
