user_prompt = "Please enter add, edit show or exit: "
todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item.capitalize())
        case "edit":
            number = int(input("Number of todo to edit: "))
            new_todo = input("Enter new todo: ")
            todos.__setitem__(number - 1, new_todo)
        case "exit":
            break
print("Bye")