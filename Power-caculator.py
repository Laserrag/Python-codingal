base = int(input("Enter the base number: "))
n = int(input("Enter how many powers to calculate: "))


print(f"Powers of {base} up to {n}:/n")
for i in range(1, n + 1):
    result = base ** i
    print(f"{base}^{i} = {result}")
