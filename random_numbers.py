# Generating Pseudo Random Numbers
import random
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
count = int(input("Enter number of random numbers: "))

print("Pseudo-random numbers:")

for _ in range(count):
    print(random.randint(lower, upper), end=" ")
