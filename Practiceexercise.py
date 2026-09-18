
# problem 1 

# list = {101,105,102,101,108,105,110}
# print ( list ) # HERE NO REPETATION OF NUMBERS . 

# problem 2 
UID = [101, 102, 103]
Name = ["Alice", "BOB", "Charlie"]
Salary = [50000, 45000, 34000]

char = int(input("Enter Employee ID: "))  #  Converted to int!

if char in UID:
    index = UID.index(char)  #  Finds the matching index dynamically
    print("Employee ID is", UID[index], "| Name is", Name[index], "| Salary is", Salary[index])
else:
    print("nothing is inside")