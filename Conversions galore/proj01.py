 ###########################################################

    #  Computer Project #1

    #

    #  Algorithm

    #    Prompt user to input number of rods

    #    Convert to float

    #    Convert integer to meters, furlongs, miles, feet, and 
    #    find out how mnay minutes it takes to walk the distance

    #    Round down results

    #    Print results 

 ###########################################################
 
# Prompt user to input number of rods
stringRods = input("Input rods: ")

# Convert to float
floatRods = float(stringRods)

print("\nYou input", floatRods,"rods.\n")

print("Conversions")


# Use conversion factors provided to convert rods to meters
rodsToMeters = floatRods * 5.0292
rodsToMeters = round(rodsToMeters,3)

# Use conversion factors provided to convert rods to furlongs
rodsToFurlongs = floatRods / 40
rodsToFurlongs = round(rodsToFurlongs,3)

# Use conversion factors provided to convert rods to miles
rodsToMiles = rodsToMeters / 1609.34
rodsToMiles = round(rodsToMiles,3)

# Convert rods to feet by first converting to meters with the calculation in parentheses 
# then convert meters to feet by dividing by the given conversion factor
rodsToFeet = (floatRods * 5.0292) / .3048
rodsToFeet = round(rodsToFeet,3)


# Use given conversion factors to convert meters to miles (didn't use rodsToMiles 
# variable due to previous rounding innacuracies), then divide the miles by given
# average walking speed in units of mph and then convert to miles per minute
minutesToWalk = ((rodsToMeters / 1609.34)/ 3.1) * 60
minutesToWalk = round(minutesToWalk,3)

print("Meters:", rodsToMeters)
print("Feet:", rodsToFeet)
print("Miles:", rodsToMiles) 
print("Furlongs:", rodsToFurlongs)
print("Minutes to walk", floatRods, "rods:" , minutesToWalk)


