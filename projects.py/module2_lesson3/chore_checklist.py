total_chores = 4
orignal_count = total_chores 
print(f"You have {orignal_count} chores to finish today")
completed_count = 0
chore_num = 1
while chore_num <= total_chores:
    if chore_num  == 1:
        next_chore = "make your bed"
    elif chore_num  == 2:
        next_chore = "feed your pet"
    elif  chore_num  == 3:
        next_chore = "take out the trash"
    else:
        next_chore = "wash the dishes"
    answer = input(f"Have you finished the {next_chore} ?")
    if answer == "yes":
        completed_count+=1
        chore_num+=1 
        print("Good job.")
    else:
        print("Ok, finish it and check again.")
    print("Chores remaining : ", total_chores-completed_count)
print("All chores are completed, good job")
