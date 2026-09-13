

# n = int(input("Enter a number: "))
#
# if n % 3 == 0 or n % 5 == 0:
#     print("Divisible by 3 or 5")
# else:
#     print("Not divisible by 3 or 5")



# Finding the greatest of two numbers:


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
#
# if a > b:
#     print("Greater =", a)
# else:
#     print("Greater =", b)


# Voting eligibility of a citizen:

# age = int(input("Enter age: "))
#
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")


#finding out is this year or leap year

# year = int(input("Enter year: "))
#
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap year")
# else:
#     print("Not a leap year")


# Using IF - ELIF - ELSE

# marks = int(input("Enter marks: "))
#
# if marks >= 90:
#     print("Excellent")
#
# elif marks >= 60:
#     print("Good")
# elif marks < 40:
#     print("fail")
# else:
#     print("Need improvement")


#creating a simple calculator

# a = float(input("Enter first number: "))
# op = input("Enter operator (+, -, *, /): ")
# b = float(input("Enter second number: "))
#
# if op == "+":
#     print("Result =", a + b)
# elif op == "-":
#     print("Result =", a - b)
# elif op == "*":
#     print("Result =", a * b)
# elif op == "/":
#     print("Result =", a / b)
# else:
#     print("Invalid operator")


# using while statement

# Print numbers from 1 to 10.
# i = 0
#
# while i <= 100:
#
#
#     print(i)
#
#     i += 2

#Factorial representation

# n = int(input("Enter a number: "))
#
# factorial = 1
#
# for i in range(1, n + 1):
#     factorial = factorial * i
#
# print("Factorial =", factorial)


# largest number in a list

# numbers = [10, 25, 7, 42, 18]
# largest = numbers[0]
#
# for n in numbers:
#     if n > largest:
#         largest = n
#
# print("Largest =", largest)


# Break pass

# for i in range(1, 101):
#     if i == 60:
#         break
#     print(i)



# for i in range(1, 51):
#     if i % 5 == 0:
#         continue
#     print(i)

# Accept until zero is entered

# while True:
#     n = int(input("Enter a number (0 to stop): "))
#
#     if n == 0:
#         break
#
#     print("You entered:", n)


# pass

n = int(input("Enter a number: "))

if n > 5:
    pass
else:
    print("Number is not positive")





