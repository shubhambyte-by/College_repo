# 1. Create a list
fruits = ["apple", "banana", "mango", "orange"]
print(fruits)
# 2. Find length of a list
numbers = [10, 20, 30, 40, 50]
print(len(numbers))
# 3. Access first element
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
# 4. Access last element
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])
# 5. Access second element
numbers = [10, 20, 30, 40, 50]
print(numbers[1])
# 6. Access third element from the end
numbers = [10, 20, 30, 40, 50]
print(numbers[-3])
# 7. Change an element
numbers = [10, 20, 30, 40, 50]
numbers[2] = 100
print(numbers)
# 8. Add an element using append()
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

# 9. Insert an element	
numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)
# 10. Remove an element
numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)
# Basic Slicing
# 11. Slice first three elements
numbers = [10, 20, 30, 40, 50]
print(numbers[0:3])
# 12. Slice elements 2 to 4
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
# 13. Slice from beginning
numbers = [10, 20, 30, 40, 50]
print(numbers[:3])
# 14. Slice to the end
numbers = [10, 20, 30, 40, 50]
print(numbers[2:])
# 15. Copy the entire list using slicing
numbers = [10, 20, 30, 40, 50]
copy = numbers[:]
print(copy)
# 16. Slice using negative index
numbers = [10, 20, 30, 40, 50]
print(numbers[-4:-1])
# 17. Last three elements
numbers = [10, 20, 30, 40, 50]
print(numbers[-3:])
# 18. First four elements
numbers = [10, 20, 30, 40, 50]
print(numbers[:4])
# 19. Middle elements
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[2:5])
# 20. Select elements from index 1 to 3
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])


# Slicing with Step
# 21. Take every second element



numbers = [10, 20, 30, 40, 50, 60]
print(numbers[::2])
# 22. Take every third element



numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[::3])
# 23. Start from index 1, take every second element



numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1::2])
# 24. Slice with step 2



numbers = [10, 20, 30, 40, 50, 60]
print(numbers[0:5:2])
# 25. Slice with step 3



numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[1:7:3])
# 26. Reverse a list



numbers = [10, 20, 30, 40, 50]
print(numbers[::-1])
# 27. Reverse using negative step



numbers = [10, 20, 30, 40, 50, 60]
print(numbers[5:1:-1])
# 28. Print alternate elements in reverse



numbers = [10, 20, 30, 40, 50, 60]
print(numbers[::-2])
# 29. Reverse first four elements



numbers = [10, 20, 30, 40, 50]
print(numbers[3::-1])
# 30. Reverse last three elements



numbers = [10, 20, 30, 40, 50]
print(numbers[:1:-1])
# String Lists and Slicing
# 31. Slice a list of names



names = ["Arun", "Bala", "Charan", "Deepak", "Esha"]
print(names[1:4])
# 32. First two names



names = ["Arun", "Bala", "Charan", "Deepak", "Esha"]
print(names[:2])
# 33. Last two names



names = ["Arun", "Bala", "Charan", "Deepak", "Esha"]
print(names[-2:])
# 34. Alternate names



names = ["Arun", "Bala", "Charan", "Deepak", "Esha", "Farhan"]
print(names[::2])
# 35. Reverse names



names = ["Arun", "Bala", "Charan", "Deepak", "Esha"]
print(names[::-1])
# 36. Select names from index 1 to 3



names = ["Arun", "Bala", "Charan", "Deepak", "Esha"]
print(names[1:4])
# 37. Slice subjects



subjects = ["Python", "DBMS", "Cloud", "AI", "Gaming", "Data Science"]
print(subjects[2:5])

# 38. Alternate subjects


subjects = ["Python", "DBMS", "Cloud", "AI", "Gaming", "Data Science"]
print(subjects[::2])
# 39. Reverse subjects



subjects = ["Python", "DBMS", "Cloud", "AI", "Gaming", "Data Science"]
print(subjects[::-1])
# 40. Select last four subjects



subjects = ["Python", "DBMS", "Cloud", "AI", "Gaming", "Data Science"]
print(subjects[-4:])
# Slicing for Modification
# 41. Replace two elements



numbers = [10, 20, 30, 40, 50]
numbers[1:3] = [200, 300]
print(numbers)
# 42. Replace three elements with one element



numbers = [10, 20, 30, 40, 50]
numbers[1:4] = [100]
print(numbers)
# 43. Replace one element with multiple elements



numbers = [10, 20, 30, 40]
numbers[1:2] = [200, 300, 400]
print(numbers)
# 44. Delete elements using slicing



numbers = [10, 20, 30, 40, 50]
numbers[1:4] = []
print(numbers)
# 45. Insert elements using slicing



numbers = [10, 20, 40, 50]
numbers[2:2] = [25, 30, 35]
print(numbers)
# 46. Replace alternate elements



numbers = [10, 20, 30, 40, 50, 60]
numbers[::2] = [100, 300, 500]
print(numbers)


# 47. Delete alternate elements



numbers = [10, 20, 30, 40, 50, 60]
del numbers[::2]
print(numbers)
# 48. Make a copy and modify it



numbers = [10, 20, 30, 40, 50]
new_numbers = numbers[:]
new_numbers[0] = 999
print("Original:", numbers)
print("Copy:", new_numbers)
# 49. Extract even-position elements



numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[1::2])
# 50. Extract odd-position elements



numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[::2])
