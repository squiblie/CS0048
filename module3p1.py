def add(x,y):
    return (x+y)
def sub(x,y):
    return (x-y)
def mult(x,y):
    return (x*y)
def div(x,y):
    return (x/y)
    
while True:

    print ("1. Add")
    print ("2. Subtract")
    print ("3. Multiply")
    print ("4. Divide")
    print ("5. Exit")

    choice = int(input ("Enter your choice: "))

    if choice == 1:
        x = float(input("enter first number: "))
        y = float(input("enter second number: "))

        print ("The sum is: ", add(x,y))
    elif choice == 2:
        x = float(input("enter first number: "))
        y = float(input("enter second number: "))

        print ("The difference is: ", sub(x,y))
    elif choice == 3:
        x = float(input("enter first number: "))
        y = float(input("enter second number: "))

        print ("The product is: ", mult(x,y))
    elif choice == 4:
        x = float(input("enter first number: "))
        y = float(input("enter second number: "))

        print ("The quotient is: ", div(x,y))
    if choice == 5:
        break
    else:
        print("invalid input.")