user_prompt = "Add new member"

user_input = input(user_prompt)

file = open("../files/todos.txt", "r")
existing_members = file.readlines()
file.close()

existing_members.append(user_input + "\n")

file = open("../files/todos.txt", "w")
file.writelines(existing_members)
file.clode()



