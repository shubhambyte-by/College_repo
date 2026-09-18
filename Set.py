
# Sets And basic functions

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("A - B:", A - B)
print("B - A:", B - A)
print("Symmetric difference:", A ^ B) # (A-B)U(B-A)
A.add(7)
A.remove(1)
print(A)

C = {0, 1, 2, 3}

union = A|B|C # AUBUC
print("Union:", union)
print("Intersection:", union)

print("Symmetric difference 1 : ", B ^C)
print("Symmetric difference 2 : " , A ^C)



