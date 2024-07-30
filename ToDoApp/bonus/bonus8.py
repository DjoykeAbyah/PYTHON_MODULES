user_prompt = "Enter Password: "
password = input(user_prompt)

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digits"] = digit

uppercase = False
for letter in password:
    if letter.isupper():
        uppercase = True
result["uppercase"] = uppercase

print(result)

if all(result.values()):
    print("Strong password")
else:
    print("Weak password")



