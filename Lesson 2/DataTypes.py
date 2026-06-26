# Data types: Data types tells python what kind of value is being stored.Ex:In a school bag, we have books, water bottle, lunch box but each item has a different purpose.

age = 18 
height = 5.7 
name = "Krishiv"

print("The age is ",type(age))
print("The height is ",type(height))
print("The name is ",type(name))

#Type casting: It means changing one data type to another.Ex: Imagine u have water, water can become ice and steam that means the material is the same but the form is different.

num = 10 
print("The value of a number is", float(num))

price = 25.99
print("The value of the price is", int(price))

age1 = 18
print("The value of the age is", str(age1))

#User input: It allows the user to enter data while the program is running.Ex:Imagine an ATM, It asks for an ATM pin during runtime.(runtime means when aplication or program when its running.)

player1 = str(input("Enter your name: "))
print("Your name is", player1)

age2 = int(input("Enter your age: "))
print("Your age (again) is", age2)

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = a + b
print("The sum is ", c)

#String operations: String is a set of character.Ex:Krishiv (K = character)

#Indexing: It means acessing one character from a string.And it always counts from 0.