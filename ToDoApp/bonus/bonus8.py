date = input("Enter today's date: ")
mood = input("How would you rate your overall mood today from 1 to 10? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"../journal/{date}", 'w') as file:
    file.write(f"mood was: {mood} + 2 * \n")
    file.write(f"Thoughts of the day: {thoughts}")




