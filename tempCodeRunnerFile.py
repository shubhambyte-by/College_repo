unicode_values = input("Enter Unicode values: ")

values = unicode_values.split(",")

characters = ""

for value in values:
    characters = characters + chr(int(value))

reverse = characters[::-1]