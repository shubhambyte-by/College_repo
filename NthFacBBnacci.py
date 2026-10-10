n = int(input("Enter n: "))

if n < 0:
    print("Please enter a non-negative integer.")
elif n == 0:
    print("Fibonacci number =", 0)
elif n == 1:
    print("Fibonacci number =", 1)
else:
    a = 0
    b = 1

    for _ in range(2, n + 1):
        a, b = b, a + b
        print("Fibonacci number =", b)

    