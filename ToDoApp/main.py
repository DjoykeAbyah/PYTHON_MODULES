user_prompt = "Please enter add, edit, show, complete or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open("files/todos.txt", 'r') as file: # file would be closed by this amethod
                todos = file.readlines()  # returns list

            todos.append(todo)

            with open("files/todos.txt", 'w') as file:
                todos = file.writelines(todos)  # method for file objects

        case "show":

            with open("files/todos.txt", 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item.capitalize()}"
                print(row)

        case "edit":

            number = int(input("Number of todo to edit: ")) - 1

            with open("files/todos.txt", 'r') as file:
                todos = file.readlines()  # returns list

            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)  # Save changes back to the file

        case "complete":
            number = int(input("Number of todo to compete: "))

            with open("files/todos.txt", 'r') as file:
                todos = file.readlines()  # returns list

            todos.pop(number - 1)  # removes item with index number

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)  # Save changes back to the file

        case "exit":
            break
print("Bye")
