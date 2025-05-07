def task_manager():
    tasks = []
    
    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task description: ")
            tasks.append(task)
            print(f'Task "{task}" added.')
        
        elif choice == '2':
            task = input("Enter the task description to remove: ")
            if task in tasks:
                tasks.remove(task)
                print(f'Task "{task}" removed.')
            else:
                print(f'Task "{task}" not found.')
        
        elif choice == '3':
            if tasks:
                print("Current Tasks:")
                for t in tasks:
                    print(f"- {t}")
            else:
                print("No tasks available.")
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("invalid input.")

task_manager()
