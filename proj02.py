###############################################################################
#   Computer Project #2
#
#   Algorithm
#     Start with while loop for main program
#     prompt the user to choose the 3 options or exit
#     If user selects Speed calculator
#       Prompt user for QPU's and slope angle
#       Calculate his speed and display to user
#     If user selects Parallel universe navigator
#       Prompt user for slope angle and marios speed
#       Find PU's traveled and marios final position
#       Make sure there isn't invalid steps
#     If user selects Scuttle bug transportation
#       Prompt user for Mario's health points and coin position
#       Calculate scuttlebug position and update marios health
#     If user enters 'q' make sure program ends
#
###############################################################################
import math
#Constants variables
PROMPT = \
    "\nSelect one of the following options:\n\
    1: Speed calculator\n\
    2: Parallel Universe navigator\n\
    3: Scuttlebug transportation\n\
    q: Exit the program\n\
    Option: "

PU_SIZE = 65535
ISLAND = 1000
SCUTTLEBUG_RADIUS = 10
#Start main program while loop
x = 1
while x > 0:
    user_choice = input(PROMPT) #asks user to input choice
    if user_choice == '1': #checks if user chose 1
        #prompts user for QPU's traveled and slope angle
        QPU_travel = int(input("\nHow many QPUs do you want to travel? "))
        slope_angle = float(input("\nWhat is the angle of the slope on which Mario is standing? "))
        #calculations
        QPU_distance = PU_SIZE * 4
        user_QPU_distance = QPU_travel * QPU_distance
        speed = round(user_QPU_distance / math.cos(slope_angle))
        #displays speed
        print("\nMario needs",speed,"speed")

    elif user_choice == '2': #checks if user chose 2
        #prompts user for slope and speed
        slope = float(input("\nWhat is the angle of the slope on which Mario is standing? "))
        speed_from_user = int(input("\nWhat is Mario's speed? "))
        #calculate marios defacto speed
        defacto = speed_from_user * math.cos(slope)
        #counters
        pu = 0
        mario_pos = 0
        #for loop to check quarter steps
        for i in range(1,5):
            if (0.25 * defacto == PU_SIZE) or ((abs((0.25 * defacto + mario_pos) % PU_SIZE - PU_SIZE)) < ISLAND):
                pu += (0.25 * defacto / PU_SIZE)
                if (0.25 * defacto == PU_SIZE):
                    mario_pos = 0
                else:
                    mario_pos = ((0.25 * defacto + mario_pos) % PU_SIZE) - PU_SIZE
            else:
                print("\nQuarter step", i, "is invalid!")
                break
        if pu > 1:
            print("\nMario has travelled", round(pu), "PUs")
            print("Mario's position in this PU:", round(mario_pos))
        else:
            print("\nMario has travelled", round(pu), "PU")
            print("Mario's position in this PU:", round(mario_pos))

    elif user_choice == '3': #checks if user chose 3
        #prompt user for marios health and coint distance
        health = int(input("\nWhat is Mario's current HP? "))
        #let the user know its invalid and re-prompt till valid entry is made
        while  (1 > health) or (health > 8):
            print("\nInvalid amount of HP!")
            health = int(input("\nWhat is Mario's current HP? "))
        coin = int(input("\nAt what distance is the coin placed? Enter -1 if there is no coin. "))

        distance = health * SCUTTLEBUG_RADIUS

        if coin == -1:
            print("\nThe Scuttlebug can be transported", distance, "units of distance")
        else:
            if health == 8 and coin < SCUTTLEBUG_RADIUS:
                print("\nThe Scuttlebug can be transported", distance, "units of distance")
            elif distance >= coin:
                print("\nThe Scuttlebug can be transported", distance + SCUTTLEBUG_RADIUS, "units of distance")
            else:
                print("\nThe Scuttlebug can be transported", distance, "units of distance")

    elif user_choice == 'q': #checks if user chose q
        x = 0 #Changes x to 0 so while loop stops

















