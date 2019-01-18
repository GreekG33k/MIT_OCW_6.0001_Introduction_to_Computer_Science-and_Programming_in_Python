"""
Assignment:
Write a program that does the following in order:
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”. 
"""

# author S. Kaiafis aka Greek _G33k

import math

# Asks the user to enter a number “x”

numx = int(input("Enter number x:"))

#Asks the user to enter a number “y” 

numy = int(input ("Enter number y:"))

# Defines a function that raises number “x”, raised to the power “y”

def raise_x_to_y(numx, numy):
	result = numx ** numy
	print(numx,"**",numy,"=",result)

# # Calling function raise_x_to_y
    
raise_x_to_y(numx,numy)

log = math.log(numx,2)
#Prints out the log (base 2) of “x”
print("Log("+str(numx)+") =",log)
