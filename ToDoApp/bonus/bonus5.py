contents = ["Walk towards the door until you are close enough to reach the handle comfortably.",
            "Determine whether the door has a knob, lever, or push/pull mechanism.",
            "Turn the knob clockwise (for most doors) to disengage the latch."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)
