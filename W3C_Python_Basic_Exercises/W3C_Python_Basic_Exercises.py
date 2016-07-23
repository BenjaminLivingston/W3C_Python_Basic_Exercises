#! /usr/local/bin/python
#  ________________________________________________________________________________________
# |                                                                                        |
# | Created with Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18)                 |
# |                                                                                        |
# |     56 Basic Python Exercises                                                          |
# |     Located at: http://www.w3resource.com/python-exercises/python-basic-exercises.php  |
# |________________________________________________________________________________________|


# Import Resources
from math import pi
import sys, datetime, time, os, platform


# Main Procedure
def basicPythonExercises():
    # Instructions
    textToPrint = ('\n\t\t\t - Basic Python Exercises -'
                   '\n\n\tSelect a number 1 - 56 to see the exercise and solution.'
                   '\n\tPress any other key to exit program.')
    print('{:75}'.format(textToPrint))

    # If there is an error exit the program
    try:

        # User Selection
        if int(sys.version_info[0]) != 3:
            select = raw_input("\n\nSelection: ")
        else:
            select = input("\n\nSelection: ")

        # Exercise 01
        if str(select) == '1':
            textToPrint = ('Write a Python program to print the following string '
                           'in a specific format.'
                           '\n'
                           '\nSample String : "Twinkle, twinkle, little star, How I wonder '
                           'what you are! '
                           '\nUp above the world so high, Like a diamond in the sky. '
                           'Twinkle, twinkle, \nlittle star, How I wonder what you are"'
                           '\n\nOutput :'
                           '\nTwinkle, twinkle, little star,'
	                       '\n\tHow I wonder what you are!'
		                   '\n\t\tUp above the world so high,'
		                   '\n\t\tLike a diamond in the sky.'
                           '\nTwinkle, twinkle, little star,'
	                       '\n\tHow I wonder what you are'
                           )            
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)
            print('Twinkle, twinkle, little star,' +
                  '\n\tHow I wonder what you are!' +
                  '\n\t\tUp above the world so high,' +
                  '\n\t\tLike a diamond in the sky.' +
                  '\nTwinkle, twinkle, little star,' +
                  '\n\tHow I wonder what you are')

            # Run program again?
            seeAnotherExercise()

        # Exercise 02
        elif str(select) == '2':
            textToPrint = ('Write a Python program to get the Python version you are using.')
            exerciseInstructions(textToPrint, select)            

            # Solution
            exerciseSolution(select)
            print('You are using the ' +
                  str(sys.version_info[3]).title() + ' Release' +
                  ' of Python Version: ' +
                  str(sys.version_info[0]) + '.' +
                  str(sys.version_info[1]) + '.' +
                  str(sys.version_info[2]))

            # Run program again?
            seeAnotherExercise()
        
        # Exercise 03
        elif str(select) =='3':
            textToPrint = ('Write a Python program to display the current date and time.'
                           '\n\nSample Output :'
                           '\nCurrent date and time :'
                           '\n2014-07-05 14:34:14'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)
            currTime = time.time()
            print('Current date and time:')
            print(str(datetime.datetime.fromtimestamp(currTime).strftime('%Y-%m-%d %H:%M:%S')))

            # Run program again?
            seeAnotherExercise()

        # Exercise 04
        elif str(select) =='4':
            textToPrint = ('\nWrite a Python program which accept the radius of a circle '
                           'from the user '
                           '\nand compute the area.'
                           '\n\nSample Output :'
                           '\nr = 1.1'
                           '\nArea = 3.8013271108436504'
                           '\nnote the area of a circle is pi * radius squared'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)
            try:
                # Version 2.7 of python will require raw_input instead of input syntax
                if int(sys.version_info[0]) != 3:
                    radVar = float(raw_input("Please enter the radius of a circle as a number:  ").replace(",",""))
                else:
                    radVar = float(input("Please enter the radius of a circle as a number:  ").replace(",",""))
                piVar = float(pi)
                areaVar = float(piVar * (radVar * radVar))
                # Clear screen
                clearScreen(False, True)
                # Display output
                print('Radius = ' + str(radVar))
                print('Area = ' + str(areaVar))
            except:
                print("\nYou didn't enter a number.")

           # Run program again?
            seeAnotherExercise()

        # Exercise 05
        elif str(select) =='5':
            textToPrint = ("Write a Python program which accept the user's first "
                           "and last name and"
                           "\nprint them in reverse order with a space between them."
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)
            if int(sys.version_info[0]) != 3:
                fName = str(raw_input("Please enter your first name: "))
                lName = str(raw_input("Please enter your last name: "))
            else:
                fName = str(input("Please enter your first name: "))
                lName = str(input("Please enter your last name: "))

            # Strip leading or trailing spaces & convert to Title case
            fName = str(fName).strip()
            fName = str(fName).title()
            lName = str(lName).strip()
            lName = str(lName).title()
            # Clear Screen
            clearScreen(False, True)
            # Display output
            print('\t Exercise 5 Solution: \n')
            print('User Name: ' + lName + ' ' + fName)

            # Run program again?
            seeAnotherExercise()

        # Exercise 06
        elif str(select) =='6':
            textToPrint = ("Write a Python program which accepts a sequence of "
                           "comma-separated numbers"
                           "\nfrom user and generate a list and a tuple with those numbers."
                           "\n\nSample data : 3, 5, 7, 23"
                           "\nOutput :"
                           "\nList : ['3', ' 5', ' 7', ' 23']"
                           "\nTuple : ('3', ' 5', ' 7', ' 23')"
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)
            # Accept user list of numbers
            if int(sys.version_info[0]) != 3:
                numString = str(raw_input("Please enter a list of numbers separated by commas" +
                                          "\n(Note do not use commas in numbers greater than 1,000): "))
            else:
                numString = str(input("Please enter a list of numbers separated by commas" +
                                      "\n(Note do not use commas in numbers greater than 1,000): "))
            # Create List -- simplest solution is: numList = [n.strip() for n in numString.split(',')]
            # But, I want to make sure only numbers are included on the list
            numString = str(numString).replace(" ","")
            numList = []
            for n in numString.split(','):
                try:
                    numList.append(float(n))
                except:
                    pass
            # Create Tuple
            if int(len(numList)) != 0:
                numTuple = (numList)
                # Debug/Proving it worked
                print('List is: ', numList)
                print('Tuple is: ', numTuple)
            else:
                print('\nYou did not enter any numbers.')

            # Run program again?
            seeAnotherExercise()

        # Exercise 07
        elif str(select) =='7':
            textToPrint = ('Write a Python program to accept a filename from the '
                           'user and print the extension of it.'
                           '\n\nSample filename : abc.java'
                           '\nOutput : java'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)
            if int(sys.version_info[0]) != 3:
                fileName = raw_input("Please enter the full file name including extension: ")
            else:
                fileName = input("Please enter the full file name including extension: ")
            if fileName.find(".") > 0:
                fileExt = fileName[(fileName.rfind(".")+1):]
                # Display Output
                print('\n\nThe extension of the file is "' + str(fileExt)) + '"'
    
            #        - Alternative Solution: Select File from dialog -
            # Request key press and clear the screen before moving to alternative solution
            clearScreen(True, True)

            print('\t Exercise 7 Solution 2: \n')    
            if int(sys.version_info[0]) != 3:
                import tkFileDialog
                fileName = tkFileDialog.askopenfilename(initialdir='/', title = 'Please select a file.')
            else:
                from tkinter import filedialog
                fileName = filedialog.askopenfilename(initialdir='/', title = 'Please select a file.')
            if fileName.find(".") > 0:
                fileExt = fileName[(fileName.rfind(".")+1):]
                # Display Output
                print('\n\nThe extension of the file is "' + str(fileExt) + '"')

            # Run program again?
            seeAnotherExercise()

        # Exercise 08
        elif str(select) =='8':
            textToPrint = ('Write a Python program to display the first and '
                           'last colors from the following list.'
                           '\n\ncolor_list = ["Red","Green","White" ,"Black"]'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)
    
            colorList = ["Red","Green","White" ,"Black"]
            firstColor = str(colorList[0])
            lastColor = str(colorList[(len(colorList) - 1)])

            # Display Output
            print('The first color in the list is ' + firstColor)
            print('The last color in the list is ' + lastColor)

            # Run program again?
            seeAnotherExercise()

        # Exercise 09
        elif str(select) =='9':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 09 -
            Write a Python program to display the examination schedule. (extract the date
            from exam_st_date).
            exam_st_date = (11, 12, 2014)
            Sample Output : The examination will start from : 11 / 12 / 2014
            '''
            # Solution
            exerciseSolution(select)
    
            exam_st_date = (11, 12, 2014)
    
            # Display Output
            print('The examination will start from: %d / %d / %d'%exam_st_date)

            # Run program again?
            seeAnotherExercise()

        # Exercise 10
        elif str(select) =='10':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 10 -
            Write a Python program that accept an integer (n) and computes the value of
            n+nn+nnn.
            Sample value of n is 5
            Expected Result : 615
            '''
            # Solution
            exerciseSolution(select)
    
            try:
                # Version 2.7 of python will require raw_input instead of input syntax
                if int(sys.version_info[0]) != 3:
                    n = int(raw_input("Please enter a number:  ").replace(",",""))
                else:
                    n = int(input("Please enter a number:  ").replace(",",""))

                n1 = '{}{}'.format(n, n)
                n2 = '{}{}{}'.format(n, n, n)
                n3 = int(n) + int(n1) + int(n2)
    
                # Display Output
                print('\nResult: ' + str(n3))
            except:
                print("\nYou didn't enter a number")

            # Run program again?
            seeAnotherExercise()

        # Exercise 11
        elif str(select) =='11':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 11 -
            Write a Python program to print the documents (syntax, description etc.) of
            Python built-in function(s).
            Sample function : abs()
            Expected Result :
            abs(number) -> number
            Return the absolute value of the argument.
            '''
            # Solution
            exerciseSolution(select)

            try:
                # Version 2.7 of python will require raw_input instead of input syntax
                if int(sys.version_info[0]) != 3:
                    funcName = eval(raw_input("Enter the name of a built-in Python function:  ").replace(",",""))
                else:
                    funcName = eval(input("Enter the name of a built-in Python function:  ").replace(",",""))
                # Return Output
                print(funcName.__doc__)
            except:
                print("\nYou didn't enter a valid function name.")

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='12':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 12 -
            Write a Python program to print the calendar of a given month and year.
            Note : Use 'calendar' module.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='13':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 13 -
            Write a Python program to print the following here document.
            Sample string :
            a string that you "don't" have to escape
            This
            is a ....... multi-line
            heredoc string --------> example
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='14':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 14 -
            Write a Python program to calculate number of days between two dates.
            Sample dates : (2014, 7, 2), (2014, 7, 11)
            Expected output : 9 days
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='15':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 15 -
            Write a Python program to get the volume of a sphere with radius 6.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='16':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 16 -
            Write a Python program to get the difference between a given number and 17,
            if the number is greater than 17 return double the absolute difference.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='17':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 17 -
            Write a Python program to test whether a number is within 100 of 1000 or 2000.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='18':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 18 -
            Write a Python program to calculate the sum of three given numbers, if the
            values are equal then return thrice of their sum.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='19':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 19 -
            Write a Python program to get a new string from a given string where "Is"
            has been added to the front. If the given string already begins with "Is"
            then return the string unchanged.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='20':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 20 -
            Write a Python program to get a string which is n (non-negative integer)
            copies of a given string.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='21':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 21 -
            Write a Python program to find whether a given number (accept from the user)
            is even or odd, print out an appropriate message to the user.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='22':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 22 -
            Write a Python program to count the number 4 in a given list.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='23':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 23 -
            Write a Python program to get the n (non-negative integer) copies of the
            first 2 characters of a given sting. Return the n copies of the whole string
            if the length is less than 2.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='24':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 24 -
            Write a Python program to test whether a passed letter is a vowel or not.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='25':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 25 -
            Write a Python program to check whether a specified value is contained in a
            group of values.
            Test Data :
            3 -> [1, 5, 8, 3] : True
            -1 -> [1, 5, 8, 3] : False
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='26':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 26 -
            Write a Python program to create a histogram from a given list of integers.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='27':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 27 -
            Write a Python program to concatenate all elements in a list into a string
            and return it.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='28':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 28 -
            Write a Python program to print all even numbers from a given numbers list
            in the same order and stop the printing if any numbers that come after 237
            in the sequence.
            Sample numbers list :

            numbers = [
                386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
                399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
                815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
                958,743, 527
                ]
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='29':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 29 -
            Write a Python program to print out a set containing all the colors from
            color_list_1 which are not present in color_list_2.
            Test Data :
            color_list_1 = set(["White", "Black", "Red"])
            color_list_2 = set(["Red", "Green"])
            Expected Output :
            {'Black', 'White'}
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='30':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 30 -
            Write a Python program that will accept the base and height of a triangle
            and compute the area.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='31':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 31 -
            Write a Python program to compute the greatest common divisor (GCD) of two
            positive integers.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='32':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 32 -
            Write a Python program to get the least common multiple (LCM) of two positive
            integers.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='33':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 33 -
            Write a Python program to sum of three given integers. However, if two values
            are equal sum will be zero.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='34':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 34 -
            Write a Python program to sum of two given integers. However if the sum is
            between 15 to 20 it will return 20.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='35':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 35 -
            Write a Python program that will return true if the two given integer values
            are equal or their sum or difference is 5.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='36':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 36 -
            Write a Python program to add two objects if both objects are integer type.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='37':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 37 -
            Write a Python program to display your details like name, age, address in
            three different lines.
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='38':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 38 -
            Write a Python program to solve (x + y) * (x + y).
            Test Data : x = 4, y = 3
            Expected Output : (4 + 3) ^ 2) = 49
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='39':
            textToPrint = (''
                           )
            exerciseInstructions(textToPrint, select)
            '''
                        - 39 -
            Write a Python program to compute the future value of a specified principal
            amount, rate of interest, and number of years.
            Test Data : amt = 10000, int = 3.5, years = 7
            Expected Output : 12722.79
            '''
            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='40':
            textToPrint = ('Write a Python program to compute the distance '
                           'between the points (x1, y1) and (x2, y2).'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='41':
            textToPrint = ('Write a Python program to check whether a file exists.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='42':
            textToPrint = ('Write a Python program to determine if a Python shell is '
                           'executing in 32bit or 64bit mode on OS.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='43':
            textToPrint = ('Write a Python program to get OS name, platform and '
                           'release information.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='44':
            textToPrint = ('Write a Python program to locate Python site-packages.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='45':
            textToPrint = ('Write a python program to call an external command in Python.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='46':
            textToPrint = ('Write a python program to get the path and name of '
            'the file that is currently executing.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='47':
            textToPrint = ('Write a Python program to find out the number of CPUs using it.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='48':
            textToPrint = ('Write a Python program to parse a string to Float or Integer.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='49':
            textToPrint = ('Write a Python program to list all files of a directory in Python.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='50':
            textToPrint = ('Write a Python program to print without newline or space.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='51':
            textToPrint = ('Write a Python program to determine profiling of Python programs.'
                           '/nNote: A profile is a set of statistics that'
                           'describes how often and for how long '
                           '/nvarious parts of the program executed. These '
                           'statistics can be formatted into reports '
                           '/nvia the pstats module.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='52':
            textToPrint = ('Write a Python program to print to stderr.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='53':
            textToPrint = ('Write a python program to access environment variables.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        elif str(select) =='54':
            textToPrint = ('Write a Python program to get the current username.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='55':
            textToPrint = ('Write a Python to find local IP addresses using Python's stdlib.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()


        elif str(select) =='56':
            textToPrint = ('Write a Python program to get height and width of console window.'
                           )
            exerciseInstructions(textToPrint, select)

            # Solution
            exerciseSolution(select)

            # Run program again?
            seeAnotherExercise()

        else:
            sys.exit()
    except:
        sys.exit()


# Repeated procedures used in main procedure
def clearScreen(btnRqst, clrScrn):
    # Prompt user to enter any key after displaying output.
    if btnRqst == True:
        if int(sys.version_info[0]) != 3:
                raw_input("\n\nPress any key to continue . . . ")
        else:
            input("\n\nPress any key to continue . . . ")
    # Clear the screen.
    if clrScrn == True:
        if str(platform.system()).lower() == 'windows':
            os.system('cls')
        else:
            os.system('clear')

def exerciseInstructions(textToPrint, select):
    # Instructions for exercise with exercise number
    clearScreen(False, True)
    print('\n'+'{:^75}'.format('Exercise '+'{:02d}'.format(int(select))+':')+'\n')
    print('{:75}'.format(textToPrint))
    clearScreen(True, True)

def exerciseSolution(select):
    # Exercise Solution's label with exercise number
    print('\n'+'{:^75}'.format('Exercise '+'{:02d}'.format(int(select))+' Solution:')+'\n')

def seeAnotherExercise():
    # Repeat program?
    try:
        # Request key press and clear the screen
        clearScreen(True, True)
        if int(sys.version_info[0]) != 3:
            againTest = raw_input("\nWould you like to see another exercise? y/n: ")
        else:
            againTest = input("\nWould you like to see another exercise? y/n: ")
        if str(againTest).lower() == 'y':
            clearScreen(False, True)
            basicPythonExercises()
        else:
            sys.exit()
    except:
        sys.exit()


# Call main procedure
if __name__ == "__main__":
    basicPythonExercises()