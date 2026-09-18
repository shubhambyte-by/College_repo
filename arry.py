# numbers = [10, 20, 30, 40, 50]

# print(numbers)
# print(numbers[0])       # first element
# print(numbers[-1])      # last element
# print(len(numbers))     # number of elements
#

# reversing the array

# def reverse_array(arr):
#     left = 0
#     right = len(arr) - 1
#
#     while left < right:
#         arr[left], arr[right] = arr[right], arr[left]
#         left = left + 1
#         right =  right - 1
#
#     return arr
#
# numbers = ['A', 'B', 'C', 'D', 'E', 'F']
# print("Original:", numbers)
# print("Reversed:", reverse_array(numbers))

# number = [10,20,30,40,50]
# print("Original list:",number[0:5])
# print("reversed list:",number[::-1] )


# numbers = [10, 20, 30, 40, 50]
# numbers.reverse() #PREDEFINE FUNCTION
# print(numbers)
#
# reversed_numbers = numbers[::-1]
# print(reversed_numbers)

# Reversing the number in simpler way


# numbers = [10, 20, 30, 40, 50]
# print(numbers)
# numbers.reverse()
# print(numbers)


# def count_value(arr, target):
#     count = 0
#
#     for value in arr:
#         if value == target:
#             count += 1
#
#     return count
# i = int(input())
# numbers = [2, 5, 2, 8, 2, 9, 5]
# print("Count of ",i, "=", count_value(numbers, i))
#
# def find_maximum(arr):
#     maximum = arr[0]
#
#     for value in arr[1:]:
#         if value > maximum:
#             maximum = value
#
#     return maximum
#
# numbers = [18, 5, 27, 11, 42]
# print("Maximum =", find_maximum(numbers)) # using own function
# print("Maximum =", max(numbers)) # using build-in function
# print("Minimum = ", min(numbers))

#

# def partition(arr, pivot):
#     smaller = []
#     greater_or_equal = []
#
#     for value in arr:
#         if value < pivot:
#             smaller.append(value)
#         else:
#             greater_or_equal.append(value)
#
#     return smaller + greater_or_equal
#
# numbers = [9, 3, 7, 2, 8, 4, 6]
# print(partition(numbers, 6))

#
# Sort the values in ascending order.
# Convert k to a zero-based index using k-1.
# Return the value at that index.



# def kth_smallest(arr, k):
#     if k < 1 or k > len(arr):
#         raise ValueError("k is out of range")
#
#     sorted_arr = sorted(arr)
#     return sorted_arr[k - 1]
#
# numbers = [7, 2, 9, 4, 1, 6]
# print("Sorted:", sorted(numbers))
# print("3rd smallest:", kth_smallest(numbers, 5))

# Reverse an array without using reverse() or slicing

def reverse(arr):
    length = len(arr)
    left = 0
    right = len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original array: ", arr)
print("Reversed array: ", reverse(arr))
nums = [11,22,33,44,55,98,98,98]
find = 22
nums.insert(find,33)
nums.count(44)



