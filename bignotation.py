def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(n=int(input("Enter a number: "))))  


# Basic operation  O(1)

# One loop:

# for i = 1 to n                     O(n)

# Loop with i = i × 2                O(log n)

# Two independent loops              O(n)

# Two nested loops                   O(n²)

# Three nested loops                 O(n³)

# Divide problem by 2 repeatedly     O(log n)

# Divide + process all elements      O(n log n)

# All subsets                        O(2ⁿ)

# All permutations                   O(n!)