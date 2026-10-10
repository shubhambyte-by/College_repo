n = int(input("Enter a positive integer: "))

print("Prime factors:", end=" ")

factor = 2

while factor <= n:
    while n % factor == 0:
        print(factor, end=" ")
        n //= factor
    factor = factor + 1