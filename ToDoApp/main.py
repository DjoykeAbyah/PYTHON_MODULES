def get_todos():
    with open("files/todos.txt", 'r') as file_local:  # file would be closed by this method
        todos_local = file_local.readlines()  # returns list
    return todos_local


while True:
    user_prompt = "Please enter add, edit, show, complete or exit: "
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]  # gives part after add, list slicing operation
        todos = get_todos()
        todos.append(todo + "\n")

        with open("files/todos.txt", 'w') as file:
            todos = file.writelines(todos)  # method for file objects

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item.capitalize()}"

            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1
            todos = get_todos()
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)  # Save changes back to the file
        except ValueError:
            print("Command not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')  # removes \n from string
            todos.pop(index)  # removes item with index number

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)  # Save changes back to the file

            message = f"Todo: '{todo_to_remove}' was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command not valid. ", user_prompt)
print("Bye now")
