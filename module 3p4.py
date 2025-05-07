import random

while True:
    print("1. Play number guessing game.")
    print("2. Exit.")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        rng = random.randint(0, 100)
        print("A number has been generated between 0 and 100.")
        while True:
            user_input = int(input("Guess the number from 0 to 100: "))
            if user_input > rng:
                print("Input is greater.")
            elif user_input < rng:
                print("Input is lesser.")
            else:
                print("Number is correct!")
                break  # Exit the guessing loop after a correct guess
    elif choice == 2:
        print("Exiting the game. Goodbye!")
        break
    else:
        print("invalid input.")
