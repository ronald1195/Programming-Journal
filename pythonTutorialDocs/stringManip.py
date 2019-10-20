# String Manipulation Interactive Tutorial

# ----------------------------------------------------------------
#  						Helping functions
# ----------------------------------------------------------------


# ----------------------------------------------------------------
#  						  Display Menu
# ----------------------------------------------------------------
def displayMenu():
	print (
			"{:->55}".format("-")							+
"\nSelect one of the following options to see some magic:\n"+
		    "\n\t 1: String Creation" 						+
			"\n\t 2: Accessing elements of a String" 		+
			"\n\t 3: Getting the length of a string" 		+
			"\n\t 4: Finding elements in a string"			+
			"\n\t 5: Get count of elements in a string" 	+
			"\n\t 6: Slicing string"						+
			"\n\t 7: Splitting strings"						+
			"\n\t 8: Startswith / Endswith"					+
			"\n\t 9: Repeat Strings"						+
			"\n\t10: Replacing strings"						+
			"\n\t11: Changing Upper and Lower Case Strings" +
			"\n\t12: Reversing strings"						+
			"\n\t13: Stripping"								+
			"\n\t14: Concatenating strings"					+
			"\n\t15: Joining strings"						+
			"\n\t16: Testing strings\n"
			"{:->55}".format("-")
		  )

# ----------------------------------------------------------------
#  						 String Creation
# ----------------------------------------------------------------
def stringCreation()
	string1 = "You can declare a strings and directly assing a value to it."

	print( "\nThere are different ways to create a string:" +
		   "\n"												+
		   string1											+
		   "\n"												+
		   "Or you can ask the user for it\n"
		 )

	inputVal = raw_input("Enter a simple string: ")

	print inputVal






# ----------------------------------------------------------------
#  						  Main Function
# ----------------------------------------------------------------
def main():
	print ("\nThis is an interactive way to see what python can do" +
		   "\nwith strings.\n")
	displayMenu()
	stringCreation()

if __name__== "__main__":
  main()

