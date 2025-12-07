# Binary Operators
5 + 2
3 - 5

# Unary Operators
+12
-5

print(+12)
print(-5)

# Order of operations
# 1. **
# 2. * / // %
# 3. + -

print(2 + 3 * 2) #8
print((2 + 3) * 2) #10

# Not all fractions have a binary equivalent, so Python rounds
print(0.1)
print(0.1 + 0.1 + 0.1)

# Python works right to left for exponents (right sided binding as opposed to all other operators which have left sided binding)
print(2 ** 2 ** 3) #256 not 64 because 2^3 is 8 and 2^8 is 256
