print("Welcome to Atm cash dispencer!")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0 
customer_served =  0 
total_dispenced = 0
serving = True 
while serving : 
    name = input("Enter your name: ")
    amount = int(input("Enter your withdrawl amount : "))
    if amount <= 0:
        print("You entered an invaild amount")
        continue
    print(f"Dispencing {amount} for you")
    remaining = amount 
    idx = 1
    while idx <= 6:
        if idx == 1: value = 100
        elif idx == 2: value = 50
        elif idx == 3: value = 20
        elif idx == 4: value = 10
        elif idx == 5: value = 5
        else:
            value = 1 
        count = remaining//value
        if count > 0:
            print(count*value)
            remaining -= count*value
            if value == 100:
                total_100 += count
            elif value == 50:
                total_50 += count
            elif value == 20:
                total_20 += count
            elif value == 10:
                    total_10 += count
            elif value == 5:
                    total_5 += count
            else:
                 total_1 += count
        idx += 1 
    customer_served +=1 
    total_dispenced += amount
    print("Transaction completed")
    again = input("Next customer? Yes or No?")
    if again != "Yes":
         serving = False
print("Daily denomination report")
for slot in range(1,7):
     if slot == 1:
          value,total_100, total = 100
     elif slot == 2:
        value,total_50, total = 50
     elif slot == 3:
        value,total_20, total = 20
     elif slot == 4:
        value,total_10, total = 10
     elif slot == 5:
        value,total_5, total = 5
     else:
         value, total_1, total = 1       
     if total > 0:
         print(f"{value} unit notes dispenced : {total}")
print(f"{customer_served} : customer served") 
print(f"{total_dispenced} : total dispenced")