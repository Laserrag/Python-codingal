#

print(ord('A'))     

print(ord('a'))

print(ord('0'))

print(ord('@'))



print(chr(65))      
print(chr(97))

char = input("Enter a single character: ")

if type(char) is str and len(char) == 1:

    print("Valid input!")

else:

    print("Please enter exactly ONE character!")