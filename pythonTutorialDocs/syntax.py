# ------------------------------------------------------------------------------------
# Author: Ronald Munoz
# Description: 	This tutorial will show you some of the basic syntax concepts of 
# 		Python. Every programming language is different and it is important
# 		for you to understand what you are trying to tell the computer to do.
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# The importance of indentation
# ------------------------------------------------------------------------------------

# Let's declare an array of people for this example
roommates = ["JD", "Scott", "Matt", "Cooper"]

# Loop throught the array and check if "JD" is the value of the current iteration
for x in roommates:
	if x == "JD":
		print(x)
	else:
		print("not JD")

''' 
# Notice that if you change the indentation to 

roommates = ["JD", "Scott", "Matt", "Cooper"]

for x in roommates:
	if x == "JD":
	print(x)
	else:
	print("not JD")

# You will get a compilation error that will say

  File "syntax.py", line 15
    print(x)
        ^
IndentationError: expected an indented block

# If you add the required indentation to your code you will still get an error
# in which you will be told that the next print statement needs to be indented
# Notice that Python will only show you the top most error every single time you
# run the compiler. This is important to understand and you should take advantage
# of this learning oportunity and start developing the habit of contantly compile
# your code. This will help you catch errors in an earlier stage and will help
# you debug your code easily.

  File "syntax.py", line 17
    print("not JD")
        ^
IndentationError: expected an indented block

'''

# ------------------------------------------------------------------------------------
# Understanding variables and datatypes
# ------------------------------------------------------------------------------------