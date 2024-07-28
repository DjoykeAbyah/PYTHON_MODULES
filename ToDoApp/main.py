user_prompt = "Please enter add, edit, show, complete or exit: "
todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item.capitalize()}"
                print(row)
                print(len(todos))
        case "edit":
            number = int(input("Number of todo to edit: "))
            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo
        case "complete":
            number = int(input("Number of todo to compete: "))
            todos.pop(number)
        case "exit":
            break
print("Bye")