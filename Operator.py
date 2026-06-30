#Operators: It is a symbol that performs an operation on values or variable.Ex:[5 + 3]In this "5" and "3" are operand and "+"" is the operator. 

#Arthematic operator: It is used for calculations. 


# | Operator | Meaning | Example | Answer |

# | -------- | ------------------- | ------- | ------ |

# | +        | Addition | 5 + 3 | 8 |

# | -        | Subtraction | 10 - 4 | 6 |

# | * | Multiplication | 4 * 3 | 12 |

# | / | Division | 10 / 2 | 5.0 |

# | % | Modulus (Remainder) | 10 % 3 | 1 |

# | // | Floor Division | 10 // 3 | 3 |

# | ** | Power | 2 ** 3 | 8 |

# Easy Tricks

# +

# Add two numbers.

# -

# Subtract numbers.

# *

# Multiply numbers.

# /

# Normal division (gives decimal).

# %

# Returns the remainder.

# Real Life:

# 10 chocolates divided among 3 friends.

# Each gets 3.

# 1 chocolate remains.

# Answer = 1

# //

# Division without decimal.

# 10 chocolates ÷ 3

# Answer = 3

# **

# Power

# 2 × 2 × 2

# Answer = 8

#Comparison operator: It compares 2 values and returuns as output true or false.Ex: [a = 10] and [b = 5], then print(a > b),the result will be true.

# Operator Meaning Example Answer

# == Equal to 5 == 5 True

# != Not Equal 5 != 3 True

# > Greater Than 10 > 5 True

# < Less Than 2 < 8 True

# >= Greater Than or Equal 5 >= 5 True

# <= Less Than or Equal 3 <= 7 True

#Assigment operator: It is used to assign or update the value. 
# Assigns a value to a variable.

# +=

# Adds and assigns.

# -=

# Subtracts and assigns.

# *=

# Multiplies and assigns.

# /=

# Divides and assigns.

# %=

# Takes modulus and assigns.

# //=

# Takes floor division and assigns.

# **=

# Takes power and assigns.

# marks=90

# marks=+10// marks=marks+10//Take the current

# print(marks)

# OR

# marks=90

# num=marks+10

# print(num)

#Assignment 1

a = int(input("Enter a number: "))
b = int(input("Enter a number(again): "))

print("Addition =", a + b)
print("Subtration =", a - b)
print("Multiplication =", a * b)
print("Divison =", int(a / b))
print("Modulus =", a % b)
print("Floor Divison = ", a // b)
print("Exponent =", a ** b )

#Assigment on comparison operator

c = int(input("Enter a number: "))
d = int(input("Enter a number(again): "))

print(c == d )
print(c != d )
print(c > d )
print(c < d )
print(c >= d )
print(c <= d )

#Assignment Assignment Operator

marks = 80
marks += 10
print(marks)

marks -= 5
print(marks)

marks *= 10
print(marks)


marks /= 5
print(marks)