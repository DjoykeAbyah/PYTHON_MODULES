waiting_list = ["zara", "ana", "felice"]
waiting_list.sort()  # does not return anything

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)

waiting_list.sort(reverse=True)  # does not return anything reverse order

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)
