tasks = []


def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Tasks '{task}' added to the list.")
    # f allows you to add variables


def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter a task to delete: "))
        if taskToDelete < len(tasks) and taskToDelete >= 0:
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid input.")
        # if number is not in task lists


def listTasks():
    if not tasks:  # if tasks is empty
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):  # iterates through tasks???
            print(f"Task #{index}. {task}")


# checks if script is being run as main program
if __name__ == "__main__":
    # create a loop to run app
    print("Welcome to the todo list app :)")
    while True:
        print("")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. List Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            break
        else:
            print("Invalid input. Please try again.")

    print("Thank you for using the to do list app :)")
