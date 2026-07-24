# print("Enter a number(numerator): ")
# num = int(input())

# print("Enter a number(denominator): ")
# den = int(input())

# if num % den == 0:
#     print("\n"+str (num) + " is divisible by " + str(den))
# else:
#     print("\n"+str (num) + " is not divisible by " + str(den))

#Assignment 2

a = int(input("Enter a number: "))
b = int(input("Enter a number(again): ")) 
c = int(input("Enter a number(agin, again): "))

avg = (a + b + c) / 3
print("Average of three numbers is: ", avg)

if avg > a and avg > b and avg > c:
    print("Average is greater than all three numbers")
elif avg > a and avg > b:
    print("Average is greater than a and b")
elif avg > a and avg > c:
    print("Average is greater than a and c")
elif avg > b and avg > c:
    print("Average is greater than b and c")
elif avg > a:
    print("Average is greater than a") 
elif avg > b:
    print("Average is greater than b") 
else:
    print("Average is greater than c")

if avg >= 1000:
    print("")
