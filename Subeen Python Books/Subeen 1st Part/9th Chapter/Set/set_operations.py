A = {1, 2, 3, 4, 5}
B = {2, 4, 6, 8}

# Intersection
C = A & B 
print(C)

# Union
C = A | B
print(C)

# Items exists in one set not in both sets
C = A ^ B
print(C)

# Items exists only in A set
C = A - B
print(C)

# Items exists only in B set
C = B - A
print(C)