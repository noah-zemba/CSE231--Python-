
# Laboratory Exercise #1
#
# Purpose:  compute the two roots of a quadratic equation.
#
# Import the math module to access function "math.sqrt()".
#
import math
# **** Do not change the statement below ****

A = float( input( "\nEnter the coefficient A: " ) ) 

B = float( input( "\nEnter the coefficient B: " ) ) 

C = float( input( "\nEnter the coefficient C: " ) ) 

print( "\n\nThe coefficients of the equation:\n" ) 
print( "  Coefficient A = ", A )
print( "  Coefficient B = ", B )
print( "  Coefficient C = ", C )


# **** Replace the following with the calculations of the roots ****

root1 = (-B + math.sqrt((B**2-4*A*C)))/(2*A)  
root2 = (-B - math.sqrt((B**2-4*A*C)))/(2*A)    # replace 0.0 with the roots of the quadratic formula


print( "\nThe roots of the equation:\n" )
print( "  Root #1 = ", round(root1,3) )  # round the result to three decimal places before printing
print( "  Root #2 = ", round(root2,3) )