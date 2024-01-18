tasks = []


print("Welcome to the to do list!")


def addTask():
    add = input("What task would you like to add: ")
    tasks.append(add)
    print(f"'{add}' has been added to tasks.")


def delTask():
    try:
        listTasks()
        rm = int(input("Which # would you like to delete: "))
        tasks.pop(rm)
        print(f"'{rm}' has been deleted from tasks.")
    except:
        print('Invalid Input. Try Again.')


def listTasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i in range(len(tasks)):
            print(i, '.', tasks[i])


while True:
    print('\n')
    print("Please select one of the following options")
    print("-------------------------------------------")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. List all tasks")
    print("4. Quit")
    user = input("Enter you choice: ")

    if user == '1':
        addTask()
    elif user == '2':
        delTask()
    elif user == '3':
        listTasks()
    elif user == '4':
        break
    else:
        print("Invalid Input. Try again.")
