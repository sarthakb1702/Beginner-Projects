from datetime import datetime

def add_task():
    task=input("Enter task to add:")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    try:
        with open ("to_do_list.txt","a") as f:
            f.write(f"{task} [Added: {timestamp}]\n")
    except FileNotFoundError:
        print("File not exists")

    print(f"Task added successfully at {timestamp}")

def view_task():
    with open ("to_do_list.txt") as f:
        tasks=f.readlines()
        for i,task in enumerate(tasks,start=1):
            print(f"{i}. {task.strip()}")    

def edit_task():
    with open ("to_do_list.txt") as f:
        tasks=f.readlines()

    for i,task in enumerate(tasks,start=1):
        print(f"{i}. {task.strip()}")

    index = int(input("Enter task number you want to edit: "))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    if index >=1 and index <=len(tasks):
        edited_task=input("Enter a new task:")
        tasks[index - 1] = f"{edited_task} [Edited: {timestamp}]\n"
        with open("to_do_list.txt", "w") as f:
            f.writelines(tasks)
        print(f"Task edited successfully at {timestamp}")
    else:
        print("Invalid Task number")

def delete_task():
    with open ("to_do_list.txt") as f:
        tasks=f.readlines()

    for i,task in enumerate(tasks,start=1):
        print(f"{i}. {task.strip()}")
    
    index = int(input("Enter task number you want to delete: "))
    
    if index >=1 and index <=len(tasks):
        tasks.pop(index-1)
        with open("to_do_list.txt", "w") as file:
            file.writelines(tasks)
        print("Task deleted")
    else:
        print("Invalid Task number")

def clear_list():
    with open ("to_do_list.txt","w") as f:
        f.write("")
    print("List cleared")


while True:
    try:
        task_input=int(input(''' Enter 1 to add task
       2 to view task
       3 to edit task
       4 to delete task
       5 to clear list
       6 to exit:\n'''))
    except ValueError:
        print("Please enter a number given above")
    match task_input:
        case 1:
            add_task()
        case 2:
            view_task()
        case 3:
            edit_task()
        case 4:
            delete_task()
        case 5:
            clear_list()
        case 6:
            print("Exiting")
            break
        case _:
            print("Invalid choice... please select from the choices provided")