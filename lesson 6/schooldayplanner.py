print("smart school day planner")
print("Answer three questions and i will plan your day")
day = input("Please enter your day").strip().capitalize()
weather = input("Please enter your weather as Sunny, Cloudy or Rainy").strip().capitalize()
homework = input("Is your homework done? Yes or No?").strip().capitalize()
if day in ("Saturday","Sunday"):
    print("enjoy your weekend")
elif day == "Monday":
    print("It is the first day of the week")
elif day == "Friday":
    print("It is the last day of the school week")
elif day in("Tuesday","Wednesday","Thuersday"):
    print("It is a regular at school")
else: 
    print("Wrong input. Please check your spelling")
if weather == "Sunny" and homework == "Yes":
    print("Since the weather looks great, and your homework is done, lets go to play!")
if weather == "Cloudy" or weather == "Rainy":
    print("Not the best weather outside. Pack your umbrella")
if not (homework == "Yes"):
    print("Homework not done")
if weather == "Rainy" and not (homework == "Yes"):
    print("Its rainy outside today. Better stay home and finish your homework.")
elif weather == "Sunny" and homework == "Yes" and not (day in("Saturday","Sunday")):
    print("All set for great school day!") 
elif day in ("Saturday","Sunday") and weather == "Sunny":
    print("A great day to go to play!")
else:
    print("Take it one step at a time, you've got this!")