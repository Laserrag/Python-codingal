def greet_customer():
    print("Welcome to the Art Supplies Store!")
 
greet_customer()
 
price_per_item = float(input("Enter the price per art item in dollars: "))
items_bought = int(input("Enter the number of art items bought: "))
 
def calculate_total(price, items):
    total = price * items
    return total
 
total_cost = calculate_total(price_per_item, items_bought)

rounded_total = round(total_cost, 10)
print("Total Cost:", rounded_total)

amount_paid = float(input("Enter the amount paid by the customer: "))
 
change_due = amount_paid - rounded_total
print("Change Due: $", change_due)
 
def thank_you_message(items):
    return "Thanks for shopping at the art supplies store!"
 
print(thank_you_message(items_bought))