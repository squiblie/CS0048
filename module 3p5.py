def main():
    scores = []
    
    while True:
        print("1. Add Score")
        print("2. Calculate Average")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            subject = input("Enter the subject name: ")
            try:
                score = float(input(f"Enter the score for {subject}: "))
                scores.append(score)
                print(f"Score of {score} added for {subject}.")
            except ValueError:
                print("Invalid input. Please enter a numeric score.")
        
        elif choice == '2':
            if scores:
                average = sum(scores) / len(scores)
                print(f"The average score is: {average:.2f}")
            else:
                print("No scores available to calculate the average.")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("invalid input.")
            
if __name__ == "__main__":
    main()
