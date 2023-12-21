###############################################################################
#   Computer Project #1
#
#   Algorithm
#     Prompt for a float value of rods
#     Print the value of rods
#     Convert the value of rods to meters, feet, miles, and furlongs
#     Print the conversions
#     Calculate the number of minutes it takes to walk the rods from input
#     print the number of minutes it takes to walk
###############################################################################

#Asks user to input number of rods and converts to float then prints value
number_of_rods = float(input("Input rods: "))
print("\nYour value is", number_of_rods,"rods.\n")

#Converts rods to meters
rod = 5.0292
rods_to_meters = number_of_rods * rod

#convert rods to feet
meters_equal_to_one_foot = 0.3048
meters_to_feet = rods_to_meters / meters_equal_to_one_foot

#convert rods to miles
meters_equal_to_one_mile = 1609.34
meters_to_mile = rods_to_meters / meters_equal_to_one_mile

#convert rods to furlongs
rods_equal_to_one_furlong = 40
rods_to_furlong = number_of_rods / 40

#calculate minutes it takes to walk
average_walking_pace_in_mph = 3.1
hours_to_walk = meters_to_mile / 3.1
hours_to_minutes = hours_to_walk * 60

#print the calculations made
print("Conversions")
print("Meters:",round(rods_to_meters,3))
print("Feet:",round(meters_to_feet,3))
print("Miles:",round(meters_to_mile,3))
print("Furlongs:",round(rods_to_furlong,3))
print("Minutes to walk",number_of_rods,"rods:",round(hours_to_minutes,3))