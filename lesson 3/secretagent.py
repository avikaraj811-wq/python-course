name = input("What is ypur name? ")
gadget = input ("what is your favourite gadget? ")
agent_number = 8 
speed_rating = 11.5 
mission_count = 8 
heigth_m = 150 
is_active = True 
print("data type of name ", type(name))  
print("data type of gadget ", type(gadget))
print("data type of agent_number ", type(agent_number))
print("data type of speed_rating ", type(speed_rating))
print("data type of mission_count ", type(mission_count))
print("data type of height_m ", type(heigth_m))
print("data type of is_active ", type(is_active))
agent_number_text = str(agent_number)
speed_rating_text = str(speed_rating)
mission_count_text = str(mission_count)
heigth_m_text = str(heigth_m)
is_active = str(is_active) 
print(agent_number_text)
print(speed_rating_text)
print(mission_count_text)
first_three = name [0:3]
last_letter = name [-1] 
code_name = first_three + last_letter 
reversed_gadget = gadget [::-1] 
print("Agent name :  ", name ) 
print(code_name)
print(reversed_gadget)