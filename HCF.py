n = int(input("Enter an integer greater than 1: "))

divisor = 2

while divisor <= n:
    if n % divisor == 0: # dividing by 2 , and checking for reminder, if reminder is = 0 then 
        break
    divisor = divisor + 1 

print("Smallest divisor =", divisor)