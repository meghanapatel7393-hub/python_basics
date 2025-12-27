students = {}

while True:
    print("1.Add 2.View 3.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Name: ")
        marks = int(input("Marks: "))
        students[name] = marks
    elif choice == 2:
        print(students)
    else:
        break
