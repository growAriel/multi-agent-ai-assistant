def main():
    tasks = []

    while True:
        print("\nTodo List:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append({"task": task, "done": False})
            print(f"Task '{task}' added.")
        elif choice == '2':
            if tasks:
                print("Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
            else:
                print("No tasks available.")
        elif choice == '3':
            if tasks:
                task_number = int(input("Enter the task number to remove: "))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks available to remove.")
        elif choice == '4':
            print("Exiting Todo List.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# This code implements a simple Todo List application that allows users to add, view, and remove tasks. 