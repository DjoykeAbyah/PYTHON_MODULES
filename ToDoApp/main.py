user_prompt = "Please enter a todo: "
todos = []

while True:
    todo = input(user_prompt)
    # method refers to object
    print(todo.upper())
    # python method attached to data types only for lists
    todos.append(todo)
    print(todos)
