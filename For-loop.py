n = int(input("Enter the value of n: "))
print("Numbers from {0} to {1}: ".format(n,1))
for i in range(n, 0, -1):
    print(i)

#Assignment 1
a = int(input("Enter the value of a: "))
print("Numbers from {0} to {1}: ".format(a,1))
for i in range(a, -1 , -1):
    print(i)

#Assignment 2
b = int(input("Enter the value of b: "))
print("Multiplication table for {0}: ".format(b))
for i in range(1, 11):
        print(b * i)

#Assignment 3

text =input("enetr a string")
reverse=""
for i in text:
    reverse=i+reverse
print("The reversed string is: {0}".format(reverse))


n=int(input("Enter the value of n: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print("sum is ",sum)