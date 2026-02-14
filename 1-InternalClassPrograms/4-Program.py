a = int(input("enter value for star pattern: "))
c = a
b = 0
for i in range(1, a+1, 1):
    print(a * ' ' + i * " *")
    a = a - 1
for j in range(c+1, 0, -1):
    print(b * ' ' + j * " *")
    b = b + 1