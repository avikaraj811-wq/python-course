age = float(input("Please enter your age : "))
if age > 12 and age < 19 :
       print("You are a teenager.")
elif age == 10 or age == 11 or age == 12:
       print("You are approximately teenager.")
elif age == 20 :
       print("You are approximately teenager.")
elif age < 10 :
       print("You are young.")
elif age > 20 and age < 40:
       print("You are in young adulthood")
elif age > 39 and age < 66:
       print("You are middle aged.")
elif age > 65 and age < 100:
       print("You are old.")
elif age > 99:
       print("You are a superhuman!")
