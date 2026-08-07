#Assignment 1
print("ATM cash dispenser")
total_100 =  total_50 = total_20 = total_10 = 0

customer_served = 0
total_despensed =  0
serving = True

while serving:
    name = input("Enter your name: ")
    amount = int(input("Enter the amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
        continue
    print(f"Dispensing ${amount} for {name}.")
    remaining = amount
    idx = 1 
    while idx <= 6:
        if idx == 1:
            value = 100
        elif idx == 2:
            value = 50
        count = remaining // value