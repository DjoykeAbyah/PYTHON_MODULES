filenames = ["1.one", "1.two", "1.three"]

filenames = [filename.replace('.', '-') + ".txt" for filename in filenames]

print(filenames)
