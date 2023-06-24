import treadmill as tm

print("*****Initialization of the Treadmill*****")

radius = float(input("Radius of motor shaft(in meters) :- "))
rpm = float(input("RPM value :- "))

operation = tm.Instance(rpm,radius)

print("*****Get User Inputs*****")

userid = input("User ID :- ")
weight = float(input("Your weight(in kilograms) :- "))
height = float(input("Your height(in meters) :- "))
age = int(input("Your age :- "))

operation.get_user(userid,weight,height,age)

#print("*****   Press 'Y' to start  *****")

time = int(input("Running time(in seconds) :- "))

operation.get_time(time)

operation.start()

##display_speed = operation.speed
##display_distance = operation.distance
##display_calories = operation.calories
##display_steps = operation.steps

print("*****Display Outputs*****")

print("Speed :-  ", str(operation.speed))
print("Distance :-  ", str(operation.distance))
print("Calories burnt :-  ", str(operation.calories))
print("Number of steps taken :-  ", str(operation.steps))
