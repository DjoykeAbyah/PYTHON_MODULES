user_prompt = "Please enter add or show or exit: "
todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        # bitwise operator
        case "show" | "display":
            for item in todos:
                print(item.capitalize())
        case "exit":
            break
        # convention of unknown
        case _:
            print("you entered a unknown command")
print("Bye")

meals = ["pasta", "pizza", "potato"]

for meal in meals:
    print(meal.capitalize())

print("Bye")

meals = ["pasta", "pizza", "potato"]


for char in "meals":
    print(meal.capitalize())

print("Bye")