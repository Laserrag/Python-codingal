# Program to swap 3 values

# Input values
a = 10
b = 20
c = 30

print("Before swapping:")
print("a =", a, "b =", b, "c =", c)

# Swapping logic
# Let's rotate them so that a → b, b → c, c → a
a, b, c = c, a, b

print("\nAfter swapping:")
print("a =", a, "b =", b, "c =", c)
