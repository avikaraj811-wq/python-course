field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110
total = field1 + field2 + field3 + field4+ field5 
average = total/5 
print("total produce : ", total,"kg")
print("average per field : ", average, "kg")
price_per_kg = 15 
earnings = total * price_per_kg 
print("total earnings : Rs", earnings)
bags = total//25
leftover = total%25
print("total bags : ", bags)
print("leftover grain : ", leftover,"kg")
last_year = 500 
print("better than last year : ", total > last_year) 
print("same as last year? ", total == last_year)
print("atleast as good? ", total >= last_year)
total+= 30 
print("after bonus crop : ", total)
total-= 15 
print("after seed resserve : ", total) 
bags = total//25 
print("after changes, the number of bags are : ", bags)  