# Rohan wants to wear different clothes which is light and suitable for weather.He will enter the temerature which then will show which clothes are suitable for wear.

temp = int(input("Please enter the temprature in celsuis :"))
if temp>= 30:
    print("You can wear a t-shirt and half pants, It is warm.")
elif temp >= 25:
    print("You can wear t-shirt and half pants, It is normal.")
elif temp >= 20:
    print("Wear a full shirt and full pant, It is cold.")
else:
    print("DON'T GO OUTSIDE!! DON'T GO OUTSIDE!! DON'T GO OUTSIDE!! DON'T GO OUTSIDE!!")