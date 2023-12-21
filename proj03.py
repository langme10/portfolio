###############################################################################
#   Computer Project #3
#
#   Algorithm
#     while loop to keep program running
#     Prompt user for input
#     input: location of house
#       User must enter Seattle, San Francisco, Austin, East Lansing
#       if they do something else it uses national averages
#       display unknown location text
#     input: desired square footage of house
#       Assume its a positive or N/A and make it a float
#     input: Max monthly payment
#       Assume its a positive or N/A and convert to float
#     input: Expected down payment
#       Assume its a positive or N/A and convert to float
#       assume numerical otherwise make float 0.0
#     input: Current APR
#       Assume user puts a value 0-100 or N/A
#       if numerical convert to float and store it as fraction
#     Ask user if they want to run program again
#
###############################################################################
import math
#Constants
NUMBER_OF_PAYMENTS = 360    # 30-year fixed rate mortgage, 30 years * 12 monthly payments
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 0.0668

WELCOME_TEXT = '''\nMORTGAGE PLANNING CALCULATOR\n============================ '''
MAIN_PROMPT = '''\nEnter a value for each of the following items or type 'NA' if unknown '''
LOCATIONS_TEXT = '''\nWhere is the house you are considering (Seattle, San Francisco, Austin, East Lansing)? '''
SQUARE_FOOTAGE_TEXT = '''\nWhat is the maximum square footage you are considering? '''
MAX_MONTHLY_PAYMENT_TEXT = '''\nWhat is the maximum monthly payment you can afford? '''
DOWN_PAYMENT_TEXT = '''\nHow much money can you put down as a down payment? '''
APR_TEXT = '''\nWhat is the current annual percentage rate? '''
AMORTIZATION_TEXT = '''\nWould you like to print the monthly payment schedule (Y or N)? '''
LOCATION_NOT_KNOWN_TEXT = '''\nUnknown location. Using national averages for price per square foot and tax rate.'''
NOT_ENOUGH_INFORMATION_TEXT = '''\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.'''
KEEP_GOING_TEXT = '''\nWould you like to make another attempt (Y or N)? '''

keep_going = "Y"
#while loop to keep program running
while keep_going == "Y":
    #welcome message
    print(WELCOME_TEXT)
    print(MAIN_PROMPT)
    #Prompt user for input
    location = input(LOCATIONS_TEXT)
    square_footage = input(SQUARE_FOOTAGE_TEXT)
    max_monthly_pay = input(MAX_MONTHLY_PAYMENT_TEXT)
    money_down = input(DOWN_PAYMENT_TEXT)
    curr_APR = input(APR_TEXT)
   #if/elif statement depending on what city the user chose
    if location == "Seattle":
        #if statement to check what info they put in
        if (square_footage != "NA") and (max_monthly_pay != "NA"):
            square_footage = float(square_footage)
            max_monthly_pay = float(max_monthly_pay)
            if money_down != "NA":
                money_down = float(money_down)
            else:
                money_down = 0.0
            if curr_APR != "NA":
                curr_APR = float(curr_APR)
            else:
                curr_APR = APR_2023 * 100
            seattle_price_square_feet_only = square_footage * SEATTLE_PRICE_PER_SQ_FOOT
            seattle_tax_pay_square_foot_only = (seattle_price_square_feet_only * SEATTLE_PROPERTY_TAX_RATE) / 12
            month_APR = curr_APR/100 / 12
            principle_amount_seattle = seattle_price_square_feet_only - money_down
            seattle_inside_exponent = (1 + month_APR) ** NUMBER_OF_PAYMENTS
            seattle_monthly_mortgage = (principle_amount_seattle * (
                        month_APR * (1 + month_APR) ** NUMBER_OF_PAYMENTS)) / (
                                                   (1 + month_APR) ** NUMBER_OF_PAYMENTS - 1)
            seattle_total = seattle_tax_pay_square_foot_only + seattle_monthly_mortgage
            # print Values
            print('\n\nIn {}, an average {:,.0f} sq. foot house would cost ${:,.0f}.'.format(location, square_footage,
                                                                                        seattle_price_square_feet_only))
            print('A 30-year fixed rate mortgage with a down payment of ${:,.0f} at {:.1f}% APR results'.format(money_down,
                                                                                                       curr_APR))
            print('\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}'.format(
                seattle_tax_pay_square_foot_only, seattle_monthly_mortgage, seattle_total))
            if max_monthly_pay > seattle_total:
                print('Based on your maximum monthly payment of ${:,.2f} you can afford this house.'.format(max_monthly_pay))
            else:
                print('Based on your maximum monthly payment of ${:,.2f} you cannot afford this house.'.format(max_monthly_pay))
            amo_text = input(AMORTIZATION_TEXT).upper()
            if amo_text == "Y":
                print('\n{:^7}|{:^12}|{:^13}|{:^14}'.format("Month", "Interest", "Payment", "Balance"))
                print("=" * 48)
                remain_loan = principle_amount_seattle
                for i in range(1, NUMBER_OF_PAYMENTS + 1):
                    pay_to_interest = remain_loan * (curr_APR/100 / 12)
                    pay_to_loan = seattle_monthly_mortgage - pay_to_interest
                    print('{:^7}| ${:>9,.2f} | ${:>10,.2f} | ${:>11,.2f}'.format(i, pay_to_interest, pay_to_loan, remain_loan))
                    remain_loan = remain_loan - pay_to_loan
        elif (square_footage != "NA"):
            #calculate cost
            square_footage = float(square_footage)
            if money_down != "NA":
                money_down = float(money_down)
            else:
                money_down = 0.0
            if curr_APR != "NA":
                curr_APR = float(curr_APR)
            else:
                curr_APR = APR_2023 * 100
            seattle_price_square_feet_only = square_footage * SEATTLE_PRICE_PER_SQ_FOOT
            seattle_tax_pay_square_foot_only = (seattle_price_square_feet_only * SEATTLE_PROPERTY_TAX_RATE)/12
            month_APR = curr_APR/100/12
            principle_amount_seattle = seattle_price_square_feet_only - money_down
            seattle_inside_exponent = (1+month_APR) ** NUMBER_OF_PAYMENTS
            seattle_monthly_mortgage = (principle_amount_seattle*(month_APR*(1+month_APR)**NUMBER_OF_PAYMENTS))/((1+month_APR)**NUMBER_OF_PAYMENTS-1)
            seattle_total = seattle_tax_pay_square_foot_only + seattle_monthly_mortgage
            #print Values
            print('\n\nIn {}, an average {:,.0f} sq. foot house would cost ${:,.0f}.'.format(location,square_footage,seattle_price_square_feet_only))
            print('A 30-year fixed rate mortgage with a down payment of ${:,.0f} at {:.1f}% APR results'.format(money_down,curr_APR))
            print('\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}'.format(seattle_tax_pay_square_foot_only,seattle_monthly_mortgage,seattle_total))
            amo_text = input(AMORTIZATION_TEXT).upper()
            if amo_text == "Y":
                print('\n{:^7}|{:^12}|{:^13}|{:^14}'.format("Month","Interest","Payment","Balance"))
                print("="*48)
                remain_loan = principle_amount_seattle
                for i in range(1,NUMBER_OF_PAYMENTS + 1):
                    pay_to_interest = remain_loan * (curr_APR/100/12)
                    pay_to_loan = seattle_monthly_mortgage - pay_to_interest
                    print('{:^7}| ${:>9,.2f} | ${:>10,.2f} | ${:>11,.2f}'.format(i,pay_to_interest,pay_to_loan,remain_loan))
                    remain_loan = remain_loan - pay_to_loan
        elif (max_monthly_pay != "NA"):
            max_monthly_pay = float(max_monthly_pay)
            if money_down != "NA":
                money_down = float(money_down)
            else:
                money_down = 0.0
            if curr_APR != "NA":
                curr_APR = float(curr_APR)
            else:
                curr_APR = APR_2023 * 100
            month_APR = curr_APR /100 / 12
            max_square_seattle = 0
            square_foot_loop = 100
            max_not_found = True
            while max_not_found:
                home_cost_loop_seattle = square_foot_loop * SEATTLE_PRICE_PER_SQ_FOOT
                principle_amount_seattle_loop = home_cost_loop_seattle - money_down
                monthly_pay_loan_loop_seattle = (principle_amount_seattle_loop*(month_APR*(1+month_APR)**NUMBER_OF_PAYMENTS))/((1+month_APR)**NUMBER_OF_PAYMENTS-1)
                monthly_pay_tax_loop_seattle = (home_cost_loop_seattle * SEATTLE_PROPERTY_TAX_RATE) / 12
                total_cost_loop_seattle = monthly_pay_tax_loop_seattle +monthly_pay_loan_loop_seattle
                if total_cost_loop_seattle > max_monthly_pay:
                    square_foot_loop -= 1
                    home_cost_loop_seattle = square_foot_loop * SEATTLE_PRICE_PER_SQ_FOOT
                    max_not_found = False
                else:
                    square_foot_loop +=1
            print('\n\nIn {}, a maximum monthly payment of ${:,.2f} allows the purchase of a house of {:,.0f} sq. feet for ${:,.0f}'.format(location,max_monthly_pay,square_foot_loop,home_cost_loop_seattle))
            print('\t assuming a 30-year fixed rate mortgage with a ${:,.0f} down payment at {:.1f}% APR.'.format(money_down,curr_APR))
        else:
            print(NOT_ENOUGH_INFORMATION_TEXT)


    elif location == "San Francisco":
        # if statement to check what info they put in
        if (square_footage != "NA") and (max_monthly_pay != "NA"):
            square_footage = float(square_footage)
            max_monthly_pay = float(max_monthly_pay)
            if money_down != "NA":
                money_down = float(money_down)
            else:
                money_down = 0.0
            if curr_APR != "NA":
                curr_APR = float(curr_APR)
            else:
                curr_APR = APR_2023 * 100
            sanfran_price_square_feet_only = square_footage * SAN_FRANCISCO_PRICE_PER_SQ_FOOT
            sanfran_tax_pay_square_foot_only = (sanfran_price_square_feet_only * SAN_FRANCISCO_PROPERTY_TAX_RATE) / 12
            month_APR = curr_APR /100 / 12
            principle_amount_sanfran = sanfran_price_square_feet_only - money_down
            sanfran_inside_exponent = (1 + month_APR) ** NUMBER_OF_PAYMENTS
            sanfran_monthly_mortgage = (principle_amount_sanfran * (month_APR * (1 + month_APR) ** NUMBER_OF_PAYMENTS)) / ((1 + month_APR) ** NUMBER_OF_PAYMENTS - 1)
            sanfran_total = sanfran_tax_pay_square_foot_only + sanfran_monthly_mortgage
            # print Values
            print('\n\nIn {}, an average {:,.0f} sq. foot house would cost ${:,.0f}.'.format(location, square_footage,sanfran_price_square_feet_only))
            print('A 30-year fixed rate mortgage with a down payment of ${:,.0f} at {:.1f}% APR results'.format(money_down,curr_APR))
            print('\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}'.format(sanfran_tax_pay_square_foot_only, sanfran_monthly_mortgage, sanfran_total))
            if max_monthly_pay > sanfran_total:
                print('Based on your maximum monthly payment of ${:,.2f} you can afford this house.'.format(max_monthly_pay))
            else:
                print('Based on your maximum monthly payment of ${:,.2f} you cannot afford this house.'.format(
                    max_monthly_pay))
            amo_text = input(AMORTIZATION_TEXT).upper()
            if amo_text == "Y":
                print('\n{:^7}|{:^12}|{:^13}|{:^14}'.format("Month", "Interest", "Payment", "Balance"))
                print("=" * 48)
                remain_loan = principle_amount_sanfran
                for i in range(1, NUMBER_OF_PAYMENTS + 1):
                    pay_to_interest = remain_loan * (curr_APR/100 / 12)
                    pay_to_loan = sanfran_monthly_mortgage - pay_to_interest
                    print('{:^7}| ${:>9,.2f} | ${:>10,.2f} | ${:>11,.2f}'.format(i, pay_to_interest, pay_to_loan,remain_loan))
                    remain_loan = remain_loan - pay_to_loan

        elif (square_footage != "NA"):

            # calculate cost

            square_footage = float(square_footage)

            if money_down != "NA":

                money_down = float(money_down)

            else:

                money_down = 0.0

            if curr_APR != "NA":

                curr_APR = float(curr_APR)

            else:

                curr_APR = APR_2023 * 100

            sanfran_price_square_feet_only = square_footage * SAN_FRANCISCO_PRICE_PER_SQ_FOOT

            sanfran_tax_pay_square_foot_only = (sanfran_price_square_feet_only * SAN_FRANCISCO_PROPERTY_TAX_RATE) / 12

            month_APR = curr_APR/100 / 12

            principle_amount_sanfran = sanfran_price_square_feet_only - money_down

            sanfran_inside_exponent = (1 + month_APR) ** NUMBER_OF_PAYMENTS

            sanfran_monthly_mortgage = (principle_amount_sanfran * (
                        month_APR * (1 + month_APR) ** NUMBER_OF_PAYMENTS)) / (
                                                   (1 + month_APR) ** NUMBER_OF_PAYMENTS - 1)

            sanfran_total = sanfran_tax_pay_square_foot_only + sanfran_monthly_mortgage

            # print Values

            print('\n\nIn {}, an average {:,.0f} sq. foot house would cost ${:,.0f}.'.format(location, square_footage,
                                                                                        sanfran_price_square_feet_only))

            print('A 30-year fixed rate mortgage with a down payment of ${:,.0f} at {:.1f}% APR results'.format(money_down,
                                                                                                       curr_APR))

            print('\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}'.format(
                sanfran_tax_pay_square_foot_only, sanfran_monthly_mortgage, sanfran_total))

            amo_text = input(AMORTIZATION_TEXT).upper()

            if amo_text == "Y":

                print('\n{:^7}|{:^12}|{:^13}|{:^14}'.format("Month", "Interest", "Payment", "Balance"))

                print("=" * 48)

                remain_loan = principle_amount_sanfran

                for i in range(1, NUMBER_OF_PAYMENTS + 1):
                    pay_to_interest = remain_loan * (curr_APR/100 / 12)

                    pay_to_loan = sanfran_monthly_mortgage - pay_to_interest

                    print('{:^7}| ${:>9,.2f} | ${:>10,.2f} | ${:>11,.2f}'.format(i, pay_to_interest, pay_to_loan,
                                                                             remain_loan))
                    remain_loan = remain_loan - pay_to_loan

        elif (max_monthly_pay != "NA"):

            max_monthly_pay = float(max_monthly_pay)

            if money_down != "NA":

                money_down = float(money_down)

            else:

                money_down = 0.0

            if curr_APR != "NA":

                curr_APR = float(curr_APR)

            else:

                curr_APR = APR_2023 * 100

            month_APR = curr_APR/100 / 12

            max_square_sanfran = 0

            square_foot_loop = 100

            max_not_found = True

            while max_not_found:

                home_cost_loop_sanfran = square_foot_loop * SAN_FRANCISCO_PRICE_PER_SQ_FOOT

                principle_amount_sanfran_loop = home_cost_loop_sanfran - money_down

                monthly_pay_loan_loop_sanfran = (principle_amount_sanfran_loop * (
                            month_APR * (1 + month_APR) ** NUMBER_OF_PAYMENTS)) / (
                                                            (1 + month_APR) ** NUMBER_OF_PAYMENTS - 1)

                monthly_pay_tax_loop_sanfran = (home_cost_loop_sanfran * SAN_FRANCISCO_PROPERTY_TAX_RATE) / 12

                total_cost_loop_sanfran = monthly_pay_tax_loop_sanfran + monthly_pay_loan_loop_sanfran

                if total_cost_loop_sanfran > max_monthly_pay:

                    square_foot_loop -= 1
                    home_cost_loop_sanfran = square_foot_loop * SAN_FRANCISCO_PRICE_PER_SQ_FOOT

                    max_not_found = False

                else:

                    square_foot_loop += 1

            print(
                '\n\nIn {}, a maximum monthly payment of ${:,.2f} allows the purchase of a house of {:,.0f} sq. feet for ${:,.0f}'.format(
                    location, max_monthly_pay, square_foot_loop, home_cost_loop_sanfran))

            print('\t assuming a 30-year fixed rate mortgage with a ${:,.0f} down payment at {:.1f}% APR.'.format(money_down,
                                                                                                         curr_APR))
        else:
            print(NOT_ENOUGH_INFORMATION_TEXT)

    elif location == "Austin":
        # if statement to check what info they put in
        if (square_footage != "NA") and (max_monthly_pay != "NA"):
            square_footage = float(square_footage)
            max_monthly_pay = float(max_monthly_pay)
            if money_down != "NA":
                money_down = float(money_down)
            else:
                money_down = 0.0
            if curr_APR != "NA":
                curr_APR = float(curr_APR)
            else:
                curr_APR = APR_2023 * 100
            austin_price_square_feet_only = square_footage * AUSTIN_PRICE_PER_SQ_FOOT
            austin_tax_pay_square_foot_only = (austin_price_square_feet_only * AUSTIN_PROPERTY_TAX_RATE) / 12
            month_APR = curr_APR/100 / 12
            principle_amount_austin = austin_price_square_feet_only - money_down
            austin_inside_exponent = (1 + month_APR) ** NUMBER_OF_PAYMENTS
            austin_monthly_mortgage = (principle_amount_austin * (
                    month_APR * (1 + month_APR) ** NUMBER_OF_PAYMENTS)) / (
                                               (1 + month_APR) ** NUMBER_OF_PAYMENTS - 1)
            austin_total = austin_tax_pay_square_foot_only + austin_monthly_mortgage
            # print Values
            print('\n\nIn {}, an average {:,.0f} sq. foot house would cost ${:,.0f}.'.format(location, square_footage,
                                                                                        austin_price_square_feet_only))
            print('A 30-year fixed rate mortgage with a down payment of ${:,.0f} at {:.1f}% APR results'.format(money_down,
                                                                                                       curr_APR))
            print('\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}'.format(
                austin_tax_pay_square_foot_only, austin_monthly_mortgage, austin_total))
            if max_monthly_pay > austin_total:
                print('Based on your maximum monthly payment of ${:,.2f} you can afford this house.'.format(max_monthly_pay))
            else:
                print('Based on your maximum monthly payment of ${:,.2f} you cannot afford this house.'.format(
                    max_monthly_pay))
            amo_text = input(AMORTIZATION_TEXT).upper()
            if amo_text == "Y":
                print('\n{:^7}|{:^12}|{:^13}|{:^14}'.format("Month", "Interest", "Payment", "Balance"))
                print("=" * 48)
                remain_loan = principle_amount_austin
                for i in range(1, NUMBER_OF_PAYMENTS + 1):
                    pay_to_interest = remain_loan * (curr_APR/100 / 12)
                    pay_to_loan = austin_monthly_mortgage - pay_to_interest

                    print('{:^7}| ${:>9,.2f} | ${:>10,.2f} | ${:>11,.2f}'.format(i, pay_to_interest, pay_to_loan,
                                                                             remain_loan))
                    remain_loan = remain_loan - pay_to_loan
        elif (square_footage != "NA"):
            # calculate cost
            square_footage = float(square_footage)
            if money_down != "NA":
                money_down = float(money_down)
            else:
                money_down = 0.0
            if curr_APR != "NA":
                curr_APR = float(curr_APR)
            else:
                curr_APR = APR_2023 * 100
            austin_price_square_feet_only = square_footage * AUSTIN_PRICE_PER_SQ_FOOT
            austin_tax_pay_square_foot_only = (austin_price_square_feet_only * SEATTLE_PROPERTY_TAX_RATE) / 12
            month_APR = curr_APR/100 / 12
            principle_amount_austin = austin_price_square_feet_only - money_down
            austin_inside_exponent = (1 + month_APR) ** NUMBER_OF_PAYMENTS
            austin_monthly_mortgage = (principle_amount_austin * (
                        month_APR * (1 + month_APR) ** NUMBER_OF_PAYMENTS)) / (
                                                   (1 + month_APR) ** NUMBER_OF_PAYMENTS - 1)
            austin_total = austin_tax_pay_square_foot_only + austin_monthly_mortgage
            # print Values
            print('\n\nIn {}, an average {:,.0f} sq. foot house would cost ${:,.0f}.'.format(location, square_footage,
                                                                                        austin_price_square_feet_only))
            print('A 30-year fixed rate mortgage with a down payment of ${:,.0f} at {:.1f}% APR results'.format(money_down,
                                                                                                       curr_APR))
            print('\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}'.format(
                austin_tax_pay_square_foot_only, austin_monthly_mortgage, austin_total))
            amo_text = input(AMORTIZATION_TEXT).upper()
            if amo_text == "Y":
                print('\n{:^7}|{:^12}|{:^13}|{:^14}'.format("Month", "Interest", "Payment", "Balance"))
                print("=" * 48)
                remain_loan = principle_amount_austin
                for i in range(1, NUMBER_OF_PAYMENTS + 1):
                    pay_to_interest = remain_loan * (curr_APR/100 / 12)
                    pay_to_loan = austin_monthly_mortgage - pay_to_interest
                    print('{:^7}| ${:>9,.2f} | ${:>10,.2f} | ${:>11,.2f}'.format(i, pay_to_interest, pay_to_loan,
                                                                             remain_loan))
                    remain_loan = remain_loan - pay_to_loan
        elif (max_monthly_pay != "NA"):
            max_monthly_pay = float(max_monthly_pay)
            if money_down != "NA":
                money_down = float(money_down)
            else:
                money_down = 0.0
            if curr_APR != "NA":
                curr_APR = float(curr_APR)
            else:
                curr_APR = APR_2023 * 100
            month_APR = curr_APR/100 / 12
            max_square_austin = 0
            square_foot_loop = 100
            max_not_found = True
            while max_not_found:
                home_cost_loop_austin = square_foot_loop * AUSTIN_PRICE_PER_SQ_FOOT
                principle_amount_austin_loop = home_cost_loop_austin - money_down
                monthly_pay_loan_loop_austin = (principle_amount_austin_loop * (
                            month_APR * (1 + month_APR) ** NUMBER_OF_PAYMENTS)) / (
                                                            (1 + month_APR) ** NUMBER_OF_PAYMENTS - 1)
                monthly_pay_tax_loop_austin = (home_cost_loop_austin * AUSTIN_PROPERTY_TAX_RATE) / 12
                total_cost_loop_austin = monthly_pay_tax_loop_austin + monthly_pay_loan_loop_austin
                if total_cost_loop_austin > max_monthly_pay:
                    square_foot_loop -= 1
                    home_cost_loop_austin = square_foot_loop * AUSTIN_PRICE_PER_SQ_FOOT
                    max_not_found = False
                else:
                    square_foot_loop += 1
            print(
                '\n\nIn {}, a maximum monthly payment of ${:,.2f} allows the purchase of a house of {:,.0f} sq. feet for ${:,.0f}'.format(
                    location, max_monthly_pay, square_foot_loop, home_cost_loop_austin))
            print('\t assuming a 30-year fixed rate mortgage with a ${:,.0f} down payment at {:.1f}% APR.'.format(money_down,
                                                                                                         curr_APR))
        else:
            print(NOT_ENOUGH_INFORMATION_TEXT)

    elif location == "East Lansing":
        # if statement to check what info they put in
        if (square_footage != "NA") and (max_monthly_pay != "NA"):
            square_footage = float(square_footage)
            max_monthly_pay = float(max_monthly_pay)
            if money_down != "NA":
                money_down = float(money_down)
            else:
                money_down = 0.0
            if curr_APR != "NA":
                curr_APR = float(curr_APR)
            else:
                curr_APR = APR_2023 * 100
            lansing_price_square_feet_only = square_footage * EAST_LANSING_PRICE_PER_SQ_FOOT
            lansing_tax_pay_square_foot_only = (lansing_price_square_feet_only * EAST_LANSING_PROPERTY_TAX_RATE) / 12
            month_APR = curr_APR /100 / 12
            principle_amount_lansing = lansing_price_square_feet_only - money_down
            lansing_inside_exponent = (1 + month_APR) ** NUMBER_OF_PAYMENTS
            lansing_monthly_mortgage = (principle_amount_lansing * (
                    month_APR * (1 + month_APR) ** NUMBER_OF_PAYMENTS)) / (
                                               (1 + month_APR) ** NUMBER_OF_PAYMENTS - 1)
            lansing_total = lansing_tax_pay_square_foot_only + lansing_monthly_mortgage
            # print Values
            print('\n\nIn {}, an average {:,.0f} sq. foot house would cost ${:,.0f}.'.format(location, square_footage,
                                                                                        lansing_price_square_feet_only))
            print('A 30-year fixed rate mortgage with a down payment of ${:,.0f} at {:.1f}% APR results'.format(money_down,
                                                                                                       curr_APR))
            print('\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}'.format(
                lansing_tax_pay_square_foot_only, lansing_monthly_mortgage, lansing_total))
            if max_monthly_pay > lansing_total:
                print('Based on your maximum monthly payment of ${:,.2f} you can afford this house.'.format(max_monthly_pay))
            else:
                print('Based on your maximum monthly payment of ${:,.2f} you cannot afford this house.'.format(
                    max_monthly_pay))
            amo_text = input(AMORTIZATION_TEXT).upper()
            if amo_text == "Y":
                print('\n{:^7}|{:^12}|{:^13}|{:^14}'.format("Month", "Interest", "Payment", "Balance"))
                print("=" * 48)
                remain_loan = principle_amount_lansing
                for i in range(1, NUMBER_OF_PAYMENTS + 1):
                    pay_to_interest = remain_loan * (curr_APR/100 / 12)
                    pay_to_loan = lansing_monthly_mortgage - pay_to_interest
                    print('{:^7}| ${:>9,.2f} | ${:>10,.2f} | ${:>11,.2f}'.format(i, pay_to_interest, pay_to_loan,
                                                                             remain_loan))
                    remain_loan = remain_loan - pay_to_loan
        elif (square_footage != "NA"):
            # calculate cost
            square_footage = float(square_footage)
            if money_down != "NA":
                money_down = float(money_down)
            else:
                money_down = 0.0
            if curr_APR != "NA":
                curr_APR = float(curr_APR)
            else:
                curr_APR = APR_2023 * 100
            lansing_price_square_feet_only = square_footage * EAST_LANSING_PRICE_PER_SQ_FOOT
            lansing_tax_pay_square_foot_only = (lansing_price_square_feet_only * EAST_LANSING_PROPERTY_TAX_RATE) / 12
            month_APR = curr_APR /100 / 12
            principle_amount_lansing = lansing_price_square_feet_only - money_down
            lansing_inside_exponent = (1 + month_APR) ** NUMBER_OF_PAYMENTS
            lansing_monthly_mortgage = (principle_amount_lansing * month_APR * (math.pow(1 + month_APR,NUMBER_OF_PAYMENTS))) / (math.pow(1 + month_APR,NUMBER_OF_PAYMENTS) - 1)
            lansing_total = lansing_tax_pay_square_foot_only + lansing_monthly_mortgage
            # print Values
            print('\n\nIn {}, an average {:,.0f} sq. foot house would cost ${:,.0f}.'.format(location, square_footage,
                                                                                        lansing_price_square_feet_only))
            print('A 30-year fixed rate mortgage with a down payment of ${:,.0f} at {:.1f}% APR results'.format(money_down,
                                                                                                       curr_APR))
            print('\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}'.format(
                lansing_tax_pay_square_foot_only, lansing_monthly_mortgage, lansing_total))
            amo_text = input(AMORTIZATION_TEXT).upper()
            if amo_text == "Y":
                print('\n{:^7}|{:^12}|{:^13}|{:^14}'.format("Month", "Interest", "Payment", "Balance"))
                print("=" * 48)
                remain_loan = principle_amount_lansing
                for i in range(1, NUMBER_OF_PAYMENTS + 1):
                    pay_to_interest = remain_loan * (curr_APR/100 / 12)
                    pay_to_loan = lansing_monthly_mortgage - pay_to_interest
                    print('{:^7}| ${:>9,.2f} | ${:>10,.2f} | ${:>11,.2f}'.format(i, pay_to_interest, pay_to_loan,
                                                                             remain_loan))
                    remain_loan = remain_loan - pay_to_loan

        elif (max_monthly_pay != "NA"):
            max_monthly_pay = float(max_monthly_pay)
            if money_down != "NA":
                money_down = float(money_down)
            else:
                money_down = 0.0
            if curr_APR != "NA":
                curr_APR = float(curr_APR)
            else:
                curr_APR = APR_2023 * 100
            month_APR = curr_APR/100 / 12
            max_square_lansing = 0
            square_foot_loop = 100
            max_not_found = True
            while max_not_found:
                home_cost_loop_lansing = square_foot_loop * EAST_LANSING_PRICE_PER_SQ_FOOT
                principle_amount_lansing_loop = home_cost_loop_lansing - money_down
                monthly_pay_loan_loop_lansing = (principle_amount_lansing_loop * (
                            month_APR * (1 + month_APR) ** NUMBER_OF_PAYMENTS)) / (
                                                            (1 + month_APR) ** NUMBER_OF_PAYMENTS - 1)
                monthly_pay_tax_loop_lansing = (home_cost_loop_lansing * EAST_LANSING_PROPERTY_TAX_RATE) / 12
                total_cost_loop_lansing = monthly_pay_tax_loop_lansing + monthly_pay_loan_loop_lansing
                if total_cost_loop_lansing > max_monthly_pay:
                    square_foot_loop -= 1
                    home_cost_loop_lansing = square_foot_loop * EAST_LANSING_PRICE_PER_SQ_FOOT
                    max_not_found = False
                else:
                    square_foot_loop += 1
            print(
                '\n\nIn {}, a maximum monthly payment of ${:,.2f} allows the purchase of a house of {:,.0f} sq. feet for ${:,.0f}'.format(
                    location, max_monthly_pay, square_foot_loop, home_cost_loop_lansing))
            print('\t assuming a 30-year fixed rate mortgage with a ${:,.0f} down payment at {:.1f}% APR.'.format(money_down,
                                                                                                         curr_APR))
        else:
            print(NOT_ENOUGH_INFORMATION_TEXT)

    else:
        print(LOCATION_NOT_KNOWN_TEXT)
        if (square_footage != "NA") and (max_monthly_pay != "NA"):
            square_footage = float(square_footage)
            max_monthly_pay = float(max_monthly_pay)
            if money_down != "NA":
                money_down = float(money_down)
            else:
                money_down = 0.0
            if curr_APR != "NA":
                curr_APR = float(curr_APR)
            else:
                curr_APR = APR_2023 * 100
            unknown_price_square_feet_only = square_footage * AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
            unknown_tax_pay_square_foot_only = (unknown_price_square_feet_only * AVERAGE_NATIONAL_PROPERTY_TAX_RATE) / 12
            month_APR = curr_APR/100/ 12
            principle_amount_unknown = unknown_price_square_feet_only - money_down
            unknown_inside_exponent = (1 + month_APR) ** NUMBER_OF_PAYMENTS
            unknown_monthly_mortgage = (principle_amount_unknown * (month_APR * (1 + month_APR) ** NUMBER_OF_PAYMENTS)) / ((1 + month_APR) ** NUMBER_OF_PAYMENTS - 1)
            unknown_total = unknown_tax_pay_square_foot_only + unknown_monthly_mortgage
            # print Values
            print('\n\nIn {}, an average {:,.0f} sq. foot house would cost ${:,.0f}.'.format(location, square_footage,
                                                                                        unknown_price_square_feet_only))
            print('A 30-year fixed rate mortgage with a down payment of ${:,.0f} at {:.1f}% APR results'.format(money_down,
                                                                                                       curr_APR))
            print('\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}'.format(
                unknown_tax_pay_square_foot_only, unknown_monthly_mortgage, unknown_total))
            if max_monthly_pay > unknown_total:
                print('Based on your maximum monthly payment of ${:,.2f} you can afford this house.'.format(max_monthly_pay))
            else:
                print('Based on your maximum monthly payment of ${:,.2f} you cannot afford this house.'.format(max_monthly_pay))
            amo_text = input(AMORTIZATION_TEXT).upper()
            if amo_text == "Y":
                print('\n{:^7}|{:^12}|{:^13}|{:^14}'.format("Month", "Interest", "Payment", "Balance"))
                print("=" * 48)
                remain_loan = principle_amount_unknown
                for i in range(1, NUMBER_OF_PAYMENTS + 1):
                    pay_to_interest = remain_loan * (curr_APR/100 / 12)
                    pay_to_loan = unknown_monthly_mortgage - pay_to_interest
                    print('{:^7}| ${:>9,.2f} | ${:>10,.2f} | ${:>11,.2f}'.format(i, pay_to_interest, pay_to_loan, remain_loan))
                    remain_loan = remain_loan - pay_to_loan
        elif (square_footage != "NA"):
            #calculate cost
            square_footage = float(square_footage)
            if money_down != "NA":
                money_down = float(money_down)
            else:
                money_down = 0.0
            if curr_APR != "NA":
                curr_APR = float(curr_APR)
            else:
                curr_APR = APR_2023 * 100
            unknown_price_square_feet_only = square_footage * AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
            unknown_tax_pay_square_foot_only = (unknown_price_square_feet_only * AVERAGE_NATIONAL_PROPERTY_TAX_RATE)/12
            month_APR = curr_APR/100/12
            principle_amount_unknown = unknown_price_square_feet_only - money_down
            unknown_inside_exponent = (1+month_APR) ** NUMBER_OF_PAYMENTS
            unknown_monthly_mortgage = (principle_amount_unknown*(month_APR*(1+month_APR)**NUMBER_OF_PAYMENTS))/((1+month_APR)**NUMBER_OF_PAYMENTS-1)
            unknown_total = unknown_tax_pay_square_foot_only + unknown_monthly_mortgage
            #print Values
            print('\n\nIn {}, an average {:,.0f} sq. foot house would cost ${:,.0f}.'.format(location,square_footage,unknown_price_square_feet_only))
            print('A 30-year fixed rate mortgage with a down payment of ${:,.0f} at {:.1f}% APR results'.format(money_down,curr_APR))
            print('\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}'.format(unknown_tax_pay_square_foot_only,unknown_monthly_mortgage,unknown_total))
            amo_text = input(AMORTIZATION_TEXT).upper()
            if amo_text == "Y":
                print('\n{:^7}|{:^12}|{:^13}|{:^14}'.format("Month","Interest","Payment","Balance"))
                print("="*48)
                remain_loan = principle_amount_unknown
                for i in range(1,NUMBER_OF_PAYMENTS + 1):
                    pay_to_interest = remain_loan * (curr_APR/100/12)
                    pay_to_loan = unknown_monthly_mortgage - pay_to_interest
                    print('{:^7}| ${:>9,.2f} | ${:>10,.2f} | ${:>11,.2f}'.format(i,pay_to_interest,pay_to_loan,remain_loan))
                    remain_loan = remain_loan - pay_to_loan
        elif (max_monthly_pay != "NA"):
            max_monthly_pay = float(max_monthly_pay)
            if money_down != "NA":
                money_down = float(money_down)
            else:
                money_down = 0.0
            if curr_APR != "NA":
                curr_APR = float(curr_APR)
            else:
                curr_APR = APR_2023 * 100
            month_APR = curr_APR /100 / 12
            max_square_seattle = 0
            square_foot_loop = 100
            max_not_found = True
            while max_not_found:
                home_cost_loop_unknown = square_foot_loop * AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
                principle_amount_unknown_loop = home_cost_loop_unknown - money_down
                monthly_pay_loan_loop_unknown = (principle_amount_unknown_loop*(month_APR*(1+month_APR)**NUMBER_OF_PAYMENTS))/((1+month_APR)**NUMBER_OF_PAYMENTS-1)
                monthly_pay_tax_loop_unknown = (home_cost_loop_unknown * AVERAGE_NATIONAL_PROPERTY_TAX_RATE) / 12
                total_cost_loop_unknown = monthly_pay_tax_loop_unknown +monthly_pay_loan_loop_unknown
                if total_cost_loop_unknown > max_monthly_pay:
                    square_foot_loop -= 1
                    home_cost_loop_unknown = square_foot_loop * AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
                    max_not_found = False
                else:
                    square_foot_loop +=1
            print('\n\nIn {}, a maximum monthly payment of ${:,.2f} allows the purchase of a house of {:,.0f} sq. feet for ${:,.0f}'.format(location,max_monthly_pay,square_foot_loop,home_cost_loop_unknown))
            print('\t assuming a 30-year fixed rate mortgage with a ${:,.0f} down payment at {:.1f}% APR.'.format(money_down,curr_APR))
        else:
            print(NOT_ENOUGH_INFORMATION_TEXT)


    #ask user if they would like to go again
    keep_going = input(KEEP_GOING_TEXT).upper()

