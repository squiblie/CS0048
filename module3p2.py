def celcius(x):
    return (x*9/5)+32
def fahrenheit(x):
    return (x-32)*5/9

while True:
    print ("1. Convert Celcius to Fahrenheit.")
    print ("2. Convert Fahrenheit to Celcius.")
    print ("3. Exit.")

    choice = int(input ("Enter your choice: "))

    if choice == 1:
        x = float(input("Enter Temperature in Celcius: "))
        print ("The Temperature in Fahrenheit is: ", celcius(x))
    elif choice == 2:
        x = float(input("Enter Temperature in Fahrenheit: "))
        print ("The Temperature in Celcius is: ", fahrenheit(y))
    elif choice == 3:
        break
    else:
        print ("invalid input.")