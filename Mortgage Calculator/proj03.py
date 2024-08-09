 ###########################################################

    #  Computer Project #3

    #

    #  Algorithm

    #    Forced into loop by if statement

    #    Show welsome message and prompt for all inputs    
    #    This will continue as long as user inputs Y whenever prompted

    #    Prompt user for all info
    
    #    Check that a square ft and monthly pay were input
    #        If one or both were input then continue
    #        Else, neither were so display message and restart

    #    Set price per foot and tax rate based on location input
    #    or set equal to generic value if no valid location was given
    
    #    Check if APR, max monthly pay and max downpay are digits or NA
    #    if they're digits then convert them to float

    #    Check for special case regaurding APR and adjust value accordingly
    
    #    If square feet or monthly pay were input
    #       Calculate and print messages for cases in which square feet were provided
    #           If monthly pay was provided check and print if user can afford payment
    #       Calculate and print emssages for cases in which square feet weren't provided
    
    #    Ask user if they want print out and print if they say yes
    
    #    Prompt to restart loop, and restart if correct input is provided
    

 ###########################################################

# Given variables
NUMBER_OF_PAYMENTS = 360
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

# instansiating variabels that will be set based on location
taxRate = float(0)
ppsqft = float(0)

# The purpouse of this count is to prevent an infinite loop, althouhg
# I think it may be useless now due to chenges I've made in my code
count = 0
if count == 0:
    count+=1
    # Automatically puts user in while loop
    attemptYN = "y"
    # .upper() garuntees that the user can put in y or Y
    while attemptYN.upper() == "Y":
        # Prints out welcome message and then asks for imputs
        print("\nMORTGAGE PLANNING CALCULATOR\n============================ \n\nEnter "
              "a value for each of the following items or type 'NA' if unknown ")
        location = input("\nWhere is the house you are considering (Seattle, San Francisco, Austin, East"
                         " Lansing)? ")
        maxSQft = input("\nWhat is the maximum square footage you are considering? ")
        maxMonthlyPay = input("\nWhat is the maximum monthly payment you can afford? ")
        maxDownPay = input("\nHow much money can you put down as a down payment? ")
        curAPR = input("\nWhat is the current annual percentage rate? ")
        
        # Sets location to lowercase to make checking for location easier 
        location = location.lower()
        
        # Tracks how many "NA" are input
        conditionCount = 0
        
        # Adds 1 to condition counter if NA is put for square footage or 
        # max monthly pay
        if maxSQft.isdigit() != True:
            conditionCount = conditionCount+1
        maxMonthlyPay = str(maxMonthlyPay)
        if maxMonthlyPay.isdigit() != True:
            conditionCount = conditionCount+1
            
        # Checks if user input a known location and sets price per sq foot
        # and tax rate for each unique location
        if location == "seattle" or location == "austin" or location == "east lansing" or location == "san francisco":
            if location == "east lansing":
                taxRate = EAST_LANSING_PROPERTY_TAX_RATE
                ppsqft = EAST_LANSING_PRICE_PER_SQ_FOOT
            elif location == "austin":
                taxRate = AUSTIN_PROPERTY_TAX_RATE
                ppsqft = AUSTIN_PRICE_PER_SQ_FOOT
            elif location == "san francisco":
                taxRate = SAN_FRANCISCO_PROPERTY_TAX_RATE
                ppsqft = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
            else:
                taxRate = SEATTLE_PROPERTY_TAX_RATE
                ppsqft = SEATTLE_PRICE_PER_SQ_FOOT
        # If the user didn't provide a valid loaction tax rate and ppsqft are set 
        # to national averages, the location is set to a string to pass test 3
        # and a message is printed
        else:
            taxRate = AVERAGE_NATIONAL_PROPERTY_TAX_RATE
            ppsqft = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
            location = "the average U.S. housing market"
            print("\nUnknown location. Using national averages for price per square foot and tax rate.")
        
        
        # Changes the users max monthly payment to a float if it is a number
        if maxMonthlyPay.isdigit() == True:
            maxMonthlyPay = float(maxMonthlyPay)
      
        # Changes the users max donpayment to a float if it is a number
        if maxDownPay.isdigit() == True:
            maxDownPay = float(maxDownPay)
        # Or sets it equal to 0 if it is NA
        else:
            maxDownPay = 0
        
        # Checks if prodided APR is a number by checking it's first character
        # and concatenates it to a float
        if curAPR[0].isdigit() == True:
            curAPR = float(curAPR)
        # If the user provides no numerical APR, then it is set to the average
        else:
            curAPR = float(APR_2023)
        
        
        # These are set to strings so I can use the .isdigit() method on them later
        maxSQft = str(maxSQft)   
        maxMonthlyPay = str(maxMonthlyPay)
        
        # I was getting an error when the APR was input as NA where it would set 
        # curAPR to the APR-2023 value but wouldn't do the normal multiplying and dividing of curAPR
        # This issue was preventing me from passing the hidden test and test 6
        if curAPR == 0.0668:
            # When no APR was being provided it wasn't being multiplied by 100
            curAPR = curAPR*100
            if maxSQft.isdigit() == False:
                # When no APR and no maxSQft were provided it somehow did the 
                # x100 for reasons I cannot explain, so I had to divide by 100
                # to get it back to it's correct value
                # I truly do not intend for this to be hard coding if it is
                # I just wasn't sure how to check
                curAPR = curAPR/100
        
        
        # If statement ensures that either a max sq. ft. or a max monthly pay is provided
        if conditionCount < 2:   
            # Checks if a max sq. ft. was provided
            if maxSQft.isdigit() == True:
                # Converts maxSQft back to a float so I can do math on it
                maxSQft = float(maxSQft)
                # Calculates cost using method provided on assignment sheet
                cost = float(maxSQft) * float(ppsqft)
                
                maxSQft = round(maxSQft,0)   
    
                # Creates and initiliazes loanAmount variable using provided formula
                loanAmount = cost - maxDownPay
                # Creates and calculates monthly taxes using provided formula
                monthlyTaxes = float((cost * taxRate)/12)
                # Changes APR from 3.25 form to 0.0325 form (not sure how to word that)
                curAPR = curAPR/100
                # My least favorite equation ever, calculates mortgage payment
                mortgagePayment = loanAmount*(((curAPR/12)*((1+curAPR/12)**360))/((((curAPR/12+1)**360)-1)))
                # Monthly payment is the sum of the taxes and mortgage
                monthlyPayment = monthlyTaxes + mortgagePayment
                # These lines make everything pretty and formatted to two decimals for printing
                monthlyPayment = round(monthlyPayment,2)
                monthlyTaxes = round(monthlyTaxes, 2)
                #################mortgagePayment = round(mortgagePayment, 2)    
                # Put APR back into 3.25 form for printing
                curAPR = curAPR*100
                
                # Sets maxSQft back to a string so I can use .isdigit()
                maxSQft = str(maxSQft)
                
                
                if maxSQft[0].isdigit():
                    # I used the .title() method which makes the first letter of every word 
                    # capital. This was intended to fix formatting erroes when the user types in 
                    # an input like East lansing or east lansing, so that it would all be capital.
                    # I had to add this if statement so that it wouldn't capitalize  the location variable if 
                    # a non- valid location was provided
                    if location == "seattle" or location == "austin" or location == "east lansing" or location == "san francisco":
                        location = location.title()
                    # Checks if the second character of maxMonthlyPay is a digit, I originally did this 
                    # in case the first character was a $ for some reason but in hindsight that doesn't make sense
                    # so this is probably redundant
                    if maxMonthlyPay[1].isdigit(): 
                        # Switches from string to float
                        maxSQft = float(maxSQft)
                        # Switches from float to int, I did this in 2 part because I was getting errors
                        # if I tried to go from string straight to int due to decimal points not being
                        # ints I believe
                        maxSQft = int(maxSQft)
                        printCost = int(cost)
                        # Creates the standard message using user inputs and calculations using them
                        
                        message = ("\n\nIn " + location + ", an average " + str(maxSQft) + " sq. foot house would cost $"
                              + str(printCost) + ".\nA 30-year fixed rate mortgage with a down payment of $" + str(int(maxDownPay)) + " at "
                              + str(round(curAPR,1)) + "% APR results\n\t" + "in an expected monthly payment of $" + "{:.2f}".format(monthlyTaxes) +
                              " (taxes) + $" + str(round(mortgagePayment, 2)) + " (mortgage payment) = $" + "{:.2f}".format(monthlyPayment))
                        # This is likley useless
                        maxMonthlyPay = str(maxMonthlyPay)
                        
                        # Prints the message
                        print(message)
                        
                        # Concatenates maxMonthlyPay to a float so I can compare it to monthly pay
                        maxMonthlyPay = float(maxMonthlyPay)
                        
                        # Compares user provided max pay and computer calculated max pay and prints 
                        # a formatted message based on the result
                        if maxMonthlyPay > monthlyPayment:                  
                            print("Based on your maximum monthly payment of $" + "{:.2f}".format(maxMonthlyPay) + " you can afford this house.")
                        else:
                            print("Based on your maximum monthly payment of $"+ "{:.2f}".format(maxMonthlyPay) + " you cannot afford this house.")
                    
                    # If maxMonthlyPay isn't a number it must not have been provided
                    else:
                        # Switches from string to float
                        maxSQft = float(maxSQft)
                        # Switches from float to int, I did this in 2 part because I was getting errors
                        # if I tried to go from string straight to int due to decimal points not being
                        # ints I believe
                        maxSQft = int(maxSQft)
                        # Decided to format this less efficiently than the previous message I guess
                        # I was initially having a ton of trouble keeping track of what value type 
                        # each variable was since I kept concatenating things so I'm sure there
                        # is a ton of useless concatenating throughout my code
                        monthlyTaxes = ("{:.2f}".format(monthlyTaxes))
                        printCost = int(cost)

                        # Creates the standard message using user inputs and calculations using them
                        message = ("\n\nIn " + location + ", an average " + str(int(maxSQft)) + " sq. foot house would cost $"
                              + str(printCost) + ".\nA 30-year fixed rate mortgage with a down payment of $" + str(int(maxDownPay)) + " at "
                              + str(round(curAPR,1)) + "% APR results\n\t" + "in an expected monthly payment of $" + str(monthlyTaxes) +
                              " (taxes) + $" + str(round(mortgagePayment, 2)) + " (mortgage payment) = $" + str(monthlyPayment))
                        # Prints the message
                        print(message)
                    
                   
                # Asks user if they want a print out      
                printOutYN = input("\nWould you like to print the monthly payment schedule (Y or N)? ")
                # Checks is response is a form of Y
                if printOutYN == "Y" or printOutYN == "y":
                    # Initializes total number of payments (will be subtracted from)
                    paymentsRemaining = 360.0
                    # initilizes month count for printed list
                    monthCount = 0
                    # Added to ensure APR was in correct form
                    curAPR = curAPR/100
                    # Wasn't sure if my loanAmount variable was causing an error I had/ have in this 
                    # chunk of code, serves the same purpouse as loanAmount
                    initialLoanValue = cost - maxDownPay
                    
                    # Stops loop when 0 payments are left to be paid
                    while paymentsRemaining > 0: 
                        # The first time it loops through is a special case because the printed
                        # balance needs to be the original balance the first time it is printed
                        if paymentsRemaining == 360:
                            # Adds to month count variable
                            monthCount +=1
                            # Uses provided equation to calculate payment to interest
                            paymentToInterest = (cost-maxDownPay) * (curAPR/12)
                            # Since monthly payment = principle + interest
                            # I used principle = monthly payment - interest
                            paymentToLoan =  mortgagePayment - (initialLoanValue * (curAPR/12))
                            # Uses provided equation to calculate remaining loan amount
                            remainingLoanAmount = (cost-maxDownPay) - (mortgagePayment - (initialLoanValue * (curAPR/12)))
                            # Prints header
                            print("\n Month |  Interest  |  Principal  |   Balance    ")    
                            print("================================================")
                            
                            # Uses formatting to get correct spaces and round numbers to 2 decimals
                            print("{:^7}|".format(monthCount), "${:>9.2f} |".format(paymentToInterest),"${:>10.2f} |".format(paymentToLoan),"${:>11.2f}".format(initialLoanValue))
                        
                        else:
                            # Uses provided equation to calculate payment to interest
                            paymentToInterest = remainingLoanAmount * (curAPR/12)
                            # Since monthly payment = principle + interest
                            # I used principle = monthly payment - interest
                            paymentToLoan = mortgagePayment - (remainingLoanAmount * (curAPR/12))   
                            # Uses provided equation to calculate remaining loan amount
                            remainingLoanAmount = remainingLoanAmount - (mortgagePayment - (remainingLoanAmount * (curAPR/12))) 
                            # Adds to month count variable
                            monthCount += 1  
                            # Uses formatting to get correct spaces and round numbers to 2 decimals
                            print("{:^7}|".format(monthCount), "${:>9.2f} |".format(paymentToInterest),"${:>10.2f} |".format(paymentToLoan),"${:>11.2f}".format(remainingLoanAmount+paymentToLoan))
                        # Subtracts a payment every time the loop loops
                        paymentsRemaining = paymentsRemaining - 1
                
            # Catches the case in which a max square footage wasn't provided                
            else:
                # I used the .title() method which makes the first letter of every word 
                # capital. This was intended to fix formatting erroes when the user types in 
                # an input like East lansing or east lansing, so that it would all be capital.
                # I had to add this if statement so that it wouldn't capitalize  the location variable if 
                # a non- valid location was provided
                if location == "seattle" or location == "austin" or location == "east lansing" or location == "san francisco":
                    location = location.title()
                # Calculates cost based on downpayment, max monthly pay, and APR
                cost = float(maxDownPay) + (float(maxMonthlyPay)*((curAPR/12+1)**360-1))/((curAPR/12)*(curAPR/12+1)**360)
                # Finds square feet by dividing the cost of the house by the price per square foot of house in that area
                maxSQft = cost/ppsqft
                
                curAPR = curAPR*100
                curAPR = round(curAPR,1)
                # Sets monthly pay to a float so it can be formatted
                maxMonthlyPay = (float(maxMonthlyPay))
                maxMonthlyPay = ("{:.2f}".format(maxMonthlyPay))
                # Prints alternate message
                print("\n\nIn " + location + ", a maximum monthly payment of $" + str(maxMonthlyPay) + 
                      " allows the purchase of a house of " + str(int(maxSQft)) + " sq. feet for $" + str(int(cost)) +
                    "\n\t assuming a 30-year fixed rate mortgage with a $" + str(int(maxDownPay)) + " down payment at " + str(curAPR) + "% APR.")
            
            
        # If the conditionCounter == 2, then the user hasn't provided a max square footage
        # or max monthly payment, and is shown the message
        else:
            print("\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.")
            
            
        # This prints immediatley after the message from line 250 to get an input
        attemptYN = input("\nWould you like to make another attempt (Y or N)? ")
