 ###########################################################

    #  Computer Project #2

    #

    #  Algorithm

    #    Prompt user to input A or B

    #    If A is input, start while loop with the condition that
    #    A continues to be input when PROMPT is asked

    #    Prompt user for Classification Code
    
    #    Check that valid code was provided, if not give try again
    #    message and promt for Classification Code again

    #    Prompt user for number of days rented, initial odometer
    #    value, and final odometer value

    #    Use values to calculate miles driven and amount due based on
    #    miles driven, days rented, and type of rental (BD, D , W)
    
    #    Prompt to restart loop, and restart if correct input is provided
    #    or break out of loop and print thank you statement
    
    #    Print thank you statement

 ###########################################################

BANNER = "\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)"

print(BANNER)


PROMPT = '''\nWould you like to continue (A/B)? '''
    
input_char = input(PROMPT)

# Booolean that tracks weather the user inputs A or B, calling A the "correct" response
correctInput = False

if input_char == "A":       
    while input_char == "A":    
        class_code = input("\nCustomer code (BD, D, W): ")
        # Checks if the classification code is one of the three provided and makes 
        # sure that the user wants to keep going with the input_char variable
        if class_code == "BD" or class_code == "D" or class_code == "W" and input_char == "A":
            # Asks user for and tracks the number of days the car was rented as an int
            numDays = int(input("\nNumber of days: "))
            # Asks user for and tracks the initial value of the odometer as an int
            iOdom = int(input("\nOdometer reading at the start: "))
            # Asks user for and tracks the final value of the odometer as an int
            fOdom = int(input("\nOdometer reading at the end:   "))
            # The difference in the initial and final values of the odometer
            # divided by 10 to convert to miles from 1/10th miles
            odomDifference = (fOdom - iOdom)/10
            # Base and mileage charges will be added up at end to give total_charge a value
            base_charge = 0.0
            mileage_charge = 0.0
            # Final charge printed
            total_charge = 0.0
            
            # This if/else statement tracks overflow within the odometer
            # if the difference is negative between the final and initial value
            # then the max value of the odometer is added to find the actual difference 
            if odomDifference < 0:
                totalMiles = float(odomDifference + 100000)
            # If the difference isn't negative, then the totalMiles will just be the 
            # final - inital odometer values converted into whole miles
            else:
                totalMiles = float((fOdom - iOdom)/10)
                
            # Checks for the case in which "BD" was input
            if class_code == "BD":
                # Adds $40 to the base charge for every day rented
                base_charge = 40 * numDays
                # Adds $0.25 to the mileage charge for every mile driven
                mileage_charge = .25 * totalMiles
            
            # Checks for the case in which "D" was input
            elif class_code == "D":
                # Divides the (final odometer value - initial odmeter value) by
                # the number of days rented input by the user
                mileagePerDay = float(totalMiles/ numDays)
                # Adds $60 to the base charge for every day rented
                base_charge = 60 * numDays
                # Checks for the case in which the average miles driven in a day is 
                # over 100
                if mileagePerDay > 100:
                    # Takes the average mileage and subtracts 100 due to the first 
                    # 100 miles being free, then multiplies by $0.25 for each mile
                    # over 100, and then multiplies by the number of days rented
                    mileage_charge = ((mileagePerDay - 100) * .25)*numDays
                    
            # Ensures that the case in which "W" is input is accounted for
            else:
                # If the total number of days rented divided by 7 has a remainder larger than 0
                if (numDays%7) > 0:
                    # Then take the amount of times 7 can do into the number of days, and add 1.
                    # This is done to account for cases where the renter doesn't rent 
                    # in increment of exact weeks, to ensure that the number is always rounded up. 
                    weeks = (numDays//7) +1
                
                # If the number of days rented divided by 7 is 0, then that is 
                # the number of weeks rented
                else:
                    weeks = float((numDays//7))
                
                # Takes the total miles and divides it by the total rounded weeks rented
                # and converts into float
                weekly_miles = float(totalMiles/(weeks))
                
                # Checks for the case in which the weekly miles is between 900 and 1500
                if 900 <= weekly_miles <= 1500:
                    # In this case, the renter's mileage charge is increased 100 per week
                    mileage_charge = float(100 * weeks)
                
                # Checks if the number of weekly miles is greater than 1500
                elif weekly_miles > 1500:
                    # If so, the renter's mileage charge is increased 200 per week and
                    # they are charged $0.25 for every mile over 1500 they drive per week rented
                    mileage_charge = float((200 * weeks)) + (((weekly_miles-1500)*.25)*weeks)
                
                # In the case that the renter drives under 900 miles weekly, they 
                # are not given a mileage charge
                elif weekly_miles < 900:
                    mileage_charge = float(0)
                
               
                # Calculates and stores the value of the base weekly rate (190) 
                # multiplied by the amount of weeks rented
                base_charge = float(190 * (weeks))
                
            # Adds base and mileage charges together to get a total bill
            total_charge = base_charge + mileage_charge
            
            # Rounds total miles and total charge to two decimal places
            printMiles = round(totalMiles,2)
            printTotal = round(total_charge,2)
            
            # Throughout printing all floats/ ints were casted to strings so they could be printed
            print("\n\nCustomer summary:")
            print("\tclassification code:", class_code)
            print("\trental period (days):", str(numDays))
            print("\todometer reading at start:", str(iOdom))
            print("\todometer reading at end:  ", str(fOdom))
            print("\tnumber of miles driven: ", str(printMiles))
            print("\tamount due: $ " + str(printTotal))
            
            # Prompts the user with continue question to restart the loop
            input_char = input(PROMPT)
            
        # If user doesn't type "BD", "D", or "W", they are shown the print statement
        # and the loop immediatley restarts with asking for Classification Code
        else:
            print("\n\t*** Invalid customer code. Try again. ***")
        
    # Accounts for the case that the user says they do not want to continue
    # after finishing at least one round of the Customer Summary
    else:
        print("\nThank you for your loyalty.")

# Accounts for the case that the user immediatley does not want to 
# continue after the banner is printed
else:       
    print("\nThank you for your loyalty.")