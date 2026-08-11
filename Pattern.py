# ************************* Pattern ************************************************
# A pattern is a design made by printing characetrs (* , #, numers ,leeters) in a sprcific shape
# ************** building rows and columns with a mnested loop *****************
# A nested loop means a loop inside another loop
# Outer loop--->rows
# inner loop ----->columns


# for row in range(3): # for rows
#     for col in range(4):
#         print("*",end="")
#     print()

# num = 1
# for row in range(4): 
#     for col in range(row + 1): 
#         print(num, end=" ")
#         num=num+1
#     print()

# n=5
# for row in range(n):
#     for col in range(n-row):
#         print("*",end=" ")
#     print()

#Assignment 1: "Right aligned triangle"

for row in range(5,0,-1):
   print(" " * (5 - row) + "*" * row)

