user_prompt = "Please enter a todo: "
todos = []


while True:
    todo = input(user_prompt)
    print(todo.title())
    todos.append(todo)

password = input("Enter password: ")

while password != "pass123":
    password = input("Enter password: ")

print("Password was correct!")

x = 1

while x <= 6:
    print(x)
    x = x + 1