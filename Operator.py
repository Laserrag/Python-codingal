# # # # #Operators: It is a symbol that performs an operation on values or variable.Ex:[5 + 3]In this "5" and "3" are operand and "+"" is the operator. 

# # # # #Arthematic operator: It is used for calculations. 


# # # # # | Operator | Meaning | Example | Answer |

# # # # # | -------- | ------------------- | ------- | ------ |

# # # # # | +        | Addition | 5 + 3 | 8 |

# # # # # | -        | Subtraction | 10 - 4 | 6 |

# # # # # | * | Multiplication | 4 * 3 | 12 |

# # # # # | / | Division | 10 / 2 | 5.0 |

# # # # # | % | Modulus (Remainder) | 10 % 3 | 1 |

# # # # # | // | Floor Division | 10 // 3 | 3 |

# # # # # | ** | Power | 2 ** 3 | 8 |

# # # # # Easy Tricks

# # # # # +

# # # # # Add two numbers.

# # # # # -

# # # # # Subtract numbers.

# # # # # *

# # # # # Multiply numbers.

# # # # # /

# # # # # Normal division (gives decimal).

# # # # # %

# # # # # Returns the remainder.

# # # # # Real Life:

# # # # # 10 chocolates divided among 3 friends.

# # # # # Each gets 3.

# # # # # 1 chocolate remains.

# # # # # Answer = 1

# # # # # //

# # # # # Division without decimal.

# # # # # 10 chocolates ÷ 3

# # # # # Answer = 3

# # # # # **

# # # # # Power

# # # # # 2 × 2 × 2

# # # # # Answer = 8

# # # # #Comparison operator: It compares 2 values and returuns as output true or false.Ex: [a = 10] and [b = 5], then print(a > b),the result will be true.

# # # # # Operator Meaning Example Answer

# # # # # == Equal to 5 == 5 True

# # # # # != Not Equal 5 != 3 True

# # # # # > Greater Than 10 > 5 True

# # # # # < Less Than 2 < 8 True

# # # # # >= Greater Than or Equal 5 >= 5 True

# # # # # <= Less Than or Equal 3 <= 7 True

# # # # #Assigment operator: It is used to assign or update the value. 
# # # # # Assigns a value to a variable.

# # # # # +=

# # # # # Adds and assigns.

# # # # # -=

# # # # # Subtracts and assigns.

# # # # # *=

# # # # # Multiplies and assigns.

# # # # # /=

# # # # # Divides and assigns.

# # # # # %=

# # # # # Takes modulus and assigns.

# # # # # //=

# # # # # Takes floor division and assigns.

# # # # # **=

# # # # # Takes power and assigns.

# # # # # marks=90

# # # # # marks=+10// marks=marks+10//Take the current

# # # # # print(marks)

# # # # # OR

# # # # # marks=90

# # # # # num=marks+10

# # # # # print(num)

# # # # #Assignment 1

# # # # a = int(input("Enter a number: "))
# # # # b = int(input("Enter a number(again): "))

# # # # print("Addition =", a + b)
# # # # print("Subtration =", a - b)
# # # # print("Multiplication =", a * b)
# # # # print("Divison =", int(a / b))
# # # # print("Modulus =", a % b)
# # # # print("Floor Divison = ", a // b)
# # # # print("Exponent =", a ** b )

# # # # #Assigment on comparison operator

# # # # c = int(input("Enter a number: "))
# # # # d = int(input("Enter a number(again): "))

# # # # print(c == d )
# # # # print(c != d )
# # # # print(c > d )
# # # # print(c < d )
# # # # print(c >= d )
# # # # print(c <= d )

# # # # #Assignment Assignment Operator

# # # # marks = 80
# # # # marks += 10
# # # # print(marks)

# # # # marks -= 5
# # # # print(marks)

# # # # marks *= 10
# # # # print(marks)


# # # # marks /= 5
# # # # print(marks)

# #Logical operators:3 operators exist in python(AND, OR, NOT)
# #AND operator:Both must be true.
# #OR operator:Any one is true
# #NOT operator:Opposite 

# a = 10
# b = 12 
# c = 0
# if  a and b and c:
#     print("All the no. have boolean value as true.")
# else:
#     print("Atleast one no. has boolean value as false.")

# d = 10
# e = -10
# f = 0
# if d > 0 or e > 0:
#     print("Either the no. is greater than 0.")
# else:
#     print("No no. is greater than 0.")

# g = 10
# h = 12
# i = 12
# print(not(g == h))

# j = 4
# k = 5
# if not((j == 1) == (k == 5)):
#     print("This is a complex program.")

# height = float(input("Enter your height in centimetre: "))
# weight =  float(input("Enter your weight in KG: "))
# bmi = weight/(height / 100)**2
# print("Your BMI is: ",bmi)

# if bmi <= 18.4:
#     print("Your under weight.")
# elif bmi <= 24.9:
#     print("You are healthy.")

# Identity operator

# it checks whether two variables refer to the same object in memory, not just wheteher they have the same value

# there are two opertaors

# 1. is

# 2 is not

# syntax

# variable1 is variable2

# variable1 is not varaible 2

# //array it is collection []

# a=[10,20,30]//creates a list

# b=a// b pioints to teh same list

# print(a is b)//true

# a=[10,20]

# b=[10,20]

# print(a is b )//false// is chceks the memory location

# print(a==b)//true // chceks values

# print(a is not b)// true //because they are differmt objects

# 2. Membership Operators

# it chcks whether an element exists inside a collection

# operators are "

# 1. in

# 2. not in

# students=["Aman","Riya","john"]// create a list

# print("isha" not in students)//true

# 3. Bit

# is the samller unit of data in a computer

# //ascii or unicode

# a=65

# A=97

# A bit can story only 0 or 1

# 4.

# Binary Numnber

# human----decimal number system

# 0 1 2 3 4 5

# computer use

# Binary number system

# 0

# 1

# 10

# 11

# 100

# 101

# Decimal to binary

# 0 0000

# 1 0001

# 2 0010

# 3 0011

# print(bin(10))

# //0b1010

# 5. bitwise opertaor

# works directly on binary numbers

# opertaor are

# &

# |

# ^(shift+6)

# ~

# <<

# >>

# 1. &

# 1 & 1 ---0

# a=5// 0101

# b=3//0011

# print(a & b)//0001