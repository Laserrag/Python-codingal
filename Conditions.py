#Identation:Identation means giving spaces before a line of code

age = 18 
if age >= 18:
    print("You can vote")

#If condition:Syntax

# if condition:
#     statement

marks = 80 
if marks>= 40:
    print("Pass!")

#If-Else statement:

# syntax:
# if condition :
#     statement 
# else :
#     statement

age1 = 17 
if age1 >= 18:
    print("You can vote")
else:
    print("You can't vote[:(]")

password = "i_am_superme_warlord_of_china"
if password == "i_am_superme_warlord_of_china":
    print("Access granted")
else:
    print("Access denied")

num = int(input("Enter a number: "))
if num >= 0:
    print("The number is positive.")
else:
    print("the number is negative.")

actual_cost  = int(input("Enter the actual cost: "))
sale_amount = int(input("Enter the sale cost: "))
profit = sale_amount - actual_cost
if profit > 0 :
    print("Your profit is", profit)
else:
    print("No profit!")

num1 = int(input("Enter a number: "))
if num1 % 2 > 0:
    print("The number is odd.")
else:
    print("The number is even.")