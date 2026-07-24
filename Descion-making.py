# Custom ride builder
choice =  int(input("Plese tell your vehicle type (1 for bike, 2 for car): "))
bike_type = int(input("Please tell your bike type (1 for city bike, 2 for mountain bike): "))
if choice == 1:
    if bike_type == 1:
        print("Bike is best for city roads.")
    else:
        print(" Car is best for off-road trails.")
elif choice == 2:
    if bike_type == 1:
        print("Bike is best for city roads.")
    else:
        print(" Car is best for off-road trails.")
elif choice == 2:
    if bike_type == 2:
        print("Bike is best for city roads.")
    else:
        print(" Car is best for off-road trails.")
else:
    print("Invalid choice. Please select 1 for bike or 2 for car.")