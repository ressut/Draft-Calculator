#Input three values - Calculate draft of vessel – Output draft and echo inputs

#Input
length = float(input("Enter Length value:"))
breadth = float(input("Enter Breadth value:"))
height = float(input("Enter Height value:"))
#Constant
iron_weight = 1.06
#Calculation
area_1 = 2*(length*height)
area_2 = 2*(breadth*height)
walls_area = area_1+area_2
floor_area = length*breadth
surface_area = walls_area+floor_area
mass = surface_area*iron_weight
draft = mass/(length*breadth)

#Output
print(f"Length: {length} Breadth: {breadth} Height: {height}")
print(f"Surface Area: {surface_area}")
print(f"Mass: {mass:.2f}")
print(f"Draft: {draft:.2f}")
