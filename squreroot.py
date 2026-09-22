# finding squre root




n = int(input("Enter a positive integer: "))

if n < 0:
    print("Square root is not defined for a negative number.")
else:
    i = 0
    while i * i <= n:
        i = i + 1
    print("Integer square root =", i-1)

# p = int(input("ENter positive  number:  "))


















# same code but short


# if p < 0:
#     print("We can not define squre root of negative number...")

# else : 
#     squre_root = p**(1/2) 
#     print("Squre root of Given number is :", squre_root)    





