todo_list = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Clear All Tasks")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        if not todo_list:
            print("\nYour to-do list is empty!")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
    elif choice == "2":
        new_task = input("Enter the task description: ")
        todo_list.append(new_task)
        print(f"'{new_task}' added successfully!")
    elif choice == "3":
        todo_list.clear()
        print("All tasks cleared!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid selection. Try again.")