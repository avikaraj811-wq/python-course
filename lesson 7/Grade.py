Science_marks = int(input("Enter your Science marks :"))
Maths_marks = int(input("Enter your Maths marks :"))
Sst_marks = int(input("Enter your Sst marks :"))
Computer_marks = int(input("Enter your Computer marks :"))
total_marks = Science_marks + Sst_marks + Computer_marks + Maths_marks 
Avarage_marks = int(total_marks / 4)
if Avarage_marks > 90:
    print("Grade A")
elif Avarage_marks > 80 & Avarage_marks < 90:
    print("Grade B ")
elif Avarage_marks > 70 & Avarage_marks < 80:
    print("Grade C")
elif Avarage_marks > 60 & Avarage_marks < 70:
    print("Grade D")
elif Avarage_marks > 50 & Avarage_marks < 60:
    print("Grade E")
else :
    print("You unfortunately failed ")
