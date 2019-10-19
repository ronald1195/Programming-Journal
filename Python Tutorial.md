<!-----------------------------------------------------------------------------------------------
Author: Ronald Munoz
Description: 	This is a personal tutorial documentation on how to get started with Python. 
              This documentation will walk you throught installations to simple programs you 
              can run in your own computer to learn how to use Python. 

              I'm learning Python with you and you might find some bugs and problems with 
              this documentation but please remember, we are learning together.
              Don't be a jerk! 
------------------------------------------------------------------------------------------------->

<!------------------------ Just a small description at the top of my file ----------------------->
```diff
# This is a small tutorial I put together for whomever wants to get started with Python and has 
# no previous experience in programming and has no idea where to start. I use a MacBook so this is 
# a Mac-specific tutorial
```

<!-----------------------------------------------------------------------------------------------
# Installations : I'm using a mac
------------------------------------------------------------------------------------------------->
# Installations
Verify if you have the software installed in your machine
* Open your terminal and type: 'python --version'. This should print something like: 'Python 2.7.13'

Macs come with a default version of Python so you might not even need to worry about this section
If you really want to install a different version of python you can follow the following steps.

- [ ] Visit python.org
- [ ] Visit the [installations page] and Download: macOS 64-bit installer


<!-----------------------------------------------------------------------------------------------  	
# How to run a simple python program
------------------------------------------------------------------------------------------------->
# How to run a simple python program
### Creating a new python file

I will be using vim for many of the simple file editing here but feel free to use any text editor you want.

```diff
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

# From this point on please notice that the version of Python I'm running is 2.7.13. Some of the sintax
# for newer versions found in the internet might not compile in your system if you run this same version
# of python.
```

Great job. That is all you need to know about creating a python file and how to run it in your system.



<!-------------------------------------------- Links ------------------------------------------>
[installations page]: https://www.python.org/downloads/release/python-380/
