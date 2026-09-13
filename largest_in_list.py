# largest number in a list

numbers = [10, 25, 7, 42, 18]
largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest =", largest)
