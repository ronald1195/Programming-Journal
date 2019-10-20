<!----------------------------------------------------------------------------------------------------------------------------
Author: Ronald Munoz
Description: 	This is a personal tutorial documentation on how to get started with Python. 
              This documentation will walk you throught installations to simple programs you 
              can run in your own computer to learn how to use Python. 

              I'm learning Python with you and you might find some bugs and problems with 
              this documentation but please remember, we are learning together.
              Don't be a jerk! 
---------------------------------------------------------------------------------------------------------------------------->

<!------------------------------------ Just a small description at the top of my file -------------------------------------->
```diff
# This is a small tutorial I put together for whomever wants to get started with Python and has 
# no previous experience in programming and has no idea where to start. I use a MacBook so this is 
# a Mac-specific tutorial
```

<!----------------------------------------------------------------------------------------------------------------------------
# Installations : I'm using a mac
---------------------------------------------------------------------------------------------------------------------------->
# Installations
Verify if you already have Python installed in your machine. ( MacBooks should )
* Open your terminal and type: 'python --version'. This should print something like: 'Python 2.7.13'

Macs come with a default version of Python so you might not even need to worry about this section
If you really want to install a different version of python you can follow the following steps.

- [ ] Visit python.org
- [ ] Visit the [installations page] and Download: macOS 64-bit installer


<!----------------------------------------------------------------------------------------------------------------------------  
# How to run a simple python program
---------------------------------------------------------------------------------------------------------------------------->
# How to run a simple python program
### Creating a new python file

I will be using vim for many of the simple file editing here but feel free to use any text editor you want.

```python
# Open your terminal and type
   
   vi helloWorld.py
   
# This will open a new file called (helloWorld.py) using vi (or vim) directly in the terminal.
# Type 'i' to enter into insert-mode in vi and type the following line

  print "Hello World!"

# Save your file. You can do thi sin vi clicking on the [esc] key and then type ':wq' to write 
# and quit editing this file. Note that typing just :w writes or saves the file and :q will quit
# it. This is not a vi tutorial so for further informatino about how to use this powerful editor 
# visit their website .. or google stuff.

# Now we need to run this file!
# In the terminal go to the directory where your python file was saved. Type:

  python helloWorld.py

# This will run your python file and will print "Hello World!" into the terminal window!
# Just as a stretch, try now to create a file with the following code in it.

  print '\n\t\tHello there!'
  print '\t\tWhat is yout name?\n'
  
  inputValue = raw_input("\tInsert your name here: ")


  print "\n\t\tHello " + inputValue + "!\n\t\tWELCOME TO PYTHON\n"

# From this point on please notice that the version of Python I'm running is 2.7.13. Some of the 
# sintax for newer versions found in the internet might not compile in your system if you run this 
# same version of python.
```

Great job. That is all you need to know about creating a python file and how to run it in your system.

<!----------------------------------------------------------------------------------------------------------------------------
# Python syntax basics
---------------------------------------------------------------------------------------------------------------------------->
# Learn the Python Syntax
## Comments
Something very important is every programming language is that you need to understand comments. Comments are one of the most basic concept of any programming languages. The compiler will ignore document comments and wont excecute anything that is recognized as a comment but they help make your code more readable and therefore, easier to maintain.

In any programming language there are two kind of comments.

**1. Single line comments**
```python

# This is a single line comment in Python

```
**2. Multi line comments**
```python

""" 

This is a 
multi line
comment. 

Everything between the " """ " is going to be a comment

"""

```
## Keywords
In Python, like in any other programming language there are some *keywords* that are reserved for the language only. Trying to use this keywords in a way the interpreter is not expecting it will result in errors.

```python

# You can check the keywords reserved for your specific version of python by simply typing the 
# following in th terminal:

>>> import keyword
>>> keyword.kwlist

# This will then print the reserved keywords for your specific version of Python

['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 
'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']

```

## Indentation
Indentation is rigidly enforced in Python. Indentation in other programming languages serves purely an organizational purpose. In Python indentation serves a hierarchy purpose and is vital that you understand how indentation works in this programming language before you attempt to write code.

```python

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

```



<!----------------------------------------------------------------------------------------------------------------------------  
# Let's learn some cool stuff about Python datatypes
---------------------------------------------------------------------------------------------------------------------------->
# Datatypes
### Strings


<!-------------------------------------------- Links ------------------------------------------>
[installations page]: https://www.python.org/downloads/release/python-380/
