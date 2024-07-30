user_prompt = "Please enter add, edit, show, complete or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if "add" in user_action or "new" in user_action:
        todo = user_action[4:]  # gives part after add, list slicing operation

        with open("files/todos.txt", 'r') as file:  # file would be closed by this method
            todos = file.readlines()  # returns list

        todos.append(todo)

        with open("files/todos.txt", 'w') as file:
            todos = file.writelines(todos)  # method for file objects

    elif "show" in user_action:

        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item.capitalize()}"

            print(row)

    elif "edit" in user_action:

        number = int(user_action[5:]) - 1

        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()  # returns list

        new_todo = input("Enter new todo: ") + "\n"
        todos[number] = new_todo

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)  # Save changes back to the file

    elif "complete" in user_action:
        number = int(user_action[9:])

        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()  # returns list

        index = number - 1
        todo_to_remove = todos[index].strip('\n')  # removes \n from string
        todos.pop(index)  # removes item with index number

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)  # Save changes back to the file

        message = f"Todo: '{todo_to_remove}' was removed from the list."
        print(message)

    elif "exit" in user_action:
        break
    else:
        print("Command not valid. ", user_prompt)
print("Bye now")
