print("Welcome to ride picker!")
print("step 1 - pick your ride")
print("1-Bike ; 2-Car")
choice = int(input("Enter 1 or 2"))
print( )
if choice == 1:
    print("Step 2 - Pick your bike ")
    print("1-Scooty ; 2-Mountain bike")
    print( )
    bike_type = int(input("Enter 1 or 2"))
    if bike_type == 1 :
        print("you picked a Scooty")
        print("Top speed = 80 kph")
        print("Best for city roads")
    else:
        print("You picked a Mountain bike")
        print("Top speed = 40 kph")
        print("Best for off roading")
elif choice == 2:
    print("step 2 - pick your car")
    print("1-Sedan; 2-SUV")
    print( )
    car_type = int(input("Enter 1 or 2"))
    if car_type == 1:
        print("You picked a Sedan")
        print("Seats 5 people")
        print("Best for family trips")
    else:
        print("You picked a SUV")
        print("Seats 7 people")
        print("Best for off-road adventures")
else :
    print("You picked the wrong choice, please try again")
print("Enjoy your journey!")