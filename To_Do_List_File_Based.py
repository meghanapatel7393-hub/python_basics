#here file does not need to manualy create its create automatically
def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")

def view_tasks():
    with open("tasks.txt", "r") as f:
        print(f.read())

while True:
    print("1.Add Task 2.View Tasks 3.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        task = input("Enter task: ")
        add_task(task)
    elif ch == 2:
        view_tasks()
    else:
        break
