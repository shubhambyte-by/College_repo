for i in range(1, 51):
    if i % 5 == 0:
        continue
    print(i)
# Accept until zero is entered

while True:
    n = int(input("Enter a number (0 to stop): "))

    if n == 0:
        break

    print("You entered:", n)
