tmp = int(input("Enter your tempertature in celsius "))
if tmp < 20:
    print("it is cold today so let's wear a jacket!")
else:
   print("it is warm today so let's wear a t-shirt! ")
is_raining = input("is it raining? Yes or No")
if is_raining == "Yes": 
    print("bring an umbrella")
wind_speed = int(input("enter your wind speed in kilometers per hour"))
if wind_speed > 30:
    print("bring a wind breaker")
else:
    print("calm today, no need for a wind breaker")
puddles = input("Are there puddles on the ground? Yes or No")
if puddles == "Yes":
    print("bring your boots.")
else:
    print("it is dry today so bring your usual sneekers")
print("Weather Outfit Check Complete") 