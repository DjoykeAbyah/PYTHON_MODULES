filenames = ["doc.txt", "report.txt", "presentation.txt"]

for filename in filenames:
    file = open(filename, "w")
    file.write("Hello")

for filename in filenames:
    file = open(filename, "r")
    line = file.readline()
    print(line)