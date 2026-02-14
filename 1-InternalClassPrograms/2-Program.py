a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))
if(a >= b and a >= c):
    print(a,"is the greatest of three!")
elif(b >= a and b >= c):
    print(b,"is the greatest of three!")
else:
    print(c,"is the greatest of three!")