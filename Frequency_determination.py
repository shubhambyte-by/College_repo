# numbers = [2, 5, 2, 8, 2, 5]

# frequency = {}

# for value in numbers:
#     frequency[value] = frequency.get(value, 0) + 1

# print(frequency)
# print("2 occurs", frequency.get(2, 0), "times")
# print("5 occurs", frequency.get(5, 0), "times")

def remove_duplicates_sorted(arr):
    if not arr:
        return []
    write = 1
    for read in range(1, len(arr)):
        if arr[read] != arr[write - 1]:
            arr[write] = arr[read]
            write += 1
    return arr[:write]

def find_maximum(arr):
    maximum = arr[0]
    for value in arr[1:]:
        if value > maximum:
            maximum = value
    return maximum

def count_value(arr, target):
    count = 0
    for value in arr:
        if value == target:
            count += 1
    return count

marks = [35, 40, 40, 55, 60, 60, 72, 85, 90]
marks.sort()
print("Unique:", remove_duplicates_sorted(marks.copy()))
print("Maximum:", find_maximum(marks))
print("60 count:", count_value(marks, 71))
print("3rd smallest:", sorted(marks)[2])