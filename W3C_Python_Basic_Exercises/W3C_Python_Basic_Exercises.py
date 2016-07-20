# Created with Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) 
'''
    56 Basic Python Exercises
    Located at: http://www.w3resource.com/python-exercises/python-basic-exercises.php

'''

# Import Resources
from sys import version_info
from math import pi
import datetime, time, os, platform


def basicPythonExercises():
    '''
                - 01 -
    Write a Python program to print the following string in a specific format.

    Sample String : "Twinkle, twinkle, little star, How I wonder what you are!
    Up above the world so high, Like a diamond in the sky. Twinkle, twinkle,
    little star, How I wonder what you are" 
    Output :
    Twinkle, twinkle, little star,
	    How I wonder what you are! 
		    Up above the world so high,   		
		    Like a diamond in the sky. 
    Twinkle, twinkle, little star, 
	    How I wonder what you are
    '''
    print('\t Exercise 1 Solution: \n')
    print('Twinkle, twinkle, little star,' +
          '\n\tHow I wonder what you are!' +
          '\n\t\tUp above the world so high,' +
          '\n\t\tLike a diamond in the sky.' +
          '\nTwinkle, twinkle, little star,' +
          '\n\tHow I wonder what you are')
    if int(version_info[0]) != 3:
            raw_input("\n\nPress any key to continue . . . ")
    else:
        input("\n\nPress any key to continue . . . ")
    if str(platform.system()).lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')


    '''
                - 02 -
    Write a Python program to get the Python version you are using.
    '''
    print('\t Exercise 2 Solution: \n')
    print('You are using the ' +
          str(version_info[3]).title() + ' Release' +
          ' of Python Version: ' +
          str(version_info[0]) + '.' +
          str(version_info[1]) + '.' +
          str(version_info[2]))
    if int(version_info[0]) != 3:
            raw_input("\n\nPress any key to continue . . . ")
    else:
        input("\n\nPress any key to continue . . . ")
    if str(platform.system()).lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')


    '''
                - 03 -
    Write a Python program to display the current date and time.
    Sample Output : 
    Current date and time : 
    2014-07-05 14:34:14
    '''
    currTime = time.time()
    print('\t Exercise 3 Solution: \n')
    print('Current date and time:')
    print(str(datetime.datetime.fromtimestamp(currTime).strftime('%Y-%m-%d %H:%M:%S')))
    if int(version_info[0]) != 3:
            raw_input("\n\nPress any key to continue . . . ")
    else:
        input("\n\nPress any key to continue . . . ")
    if str(platform.system()).lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')


    '''
                - 04 -
    Write a Python program which accept the radius of a circle from the user
    and compute the area.
    Sample Output : 
    r = 1.1
    Area = 3.8013271108436504
    note the area of a circle is pi * radius squared
    '''
    print('\t Exercise 4 Solution: \n')
    try:
        # Version 2.7 of python will require raw_input instead of input syntax
        if int(version_info[0]) != 3:
            radVar = float(raw_input("Please enter the radius of a circle as a number:  ").replace(",",""))
        else:
            radVar = float(input("Please enter the radius of a circle as a number:  ").replace(",",""))
        piVar = float(pi)
        a = float(piVar * (radVar * radVar))
        print('radius = ' + str(radVar))
        print('Area = ' + str(piVar))
    except:
        print("\nYou didn't enter a number.")
    if int(version_info[0]) != 3:
            raw_input("\n\nPress any key to continue . . . ")
    else:
        input("\n\nPress any key to continue . . . ")
    if str(platform.system()).lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')


    '''
                - 05 -
    Write a Python program which accept the user's first and last name and
    print them in reverse 
    order with a space between them.
    '''



    '''
                - 06 -
    Write a Python program which accepts a sequence of comma-separated numbers
    from user and generate a list and a tuple with those numbers.
    Sample data : 3, 5, 7, 23
    Output : 
    List : ['3', ' 5', ' 7', ' 23'] 
    Tuple : ('3', ' 5', ' 7', ' 23')
    '''



    '''
                - 07 -
    Write a Python program to accept a filename from the user print the extension
    of that.
    Sample filename : abc.java 
    Output : java
    '''



    '''
                - 08 -
    Write a Python program to display the first and last colors from the following
    list.
    color_list = ["Red","Green","White" ,"Black"]
    '''



    '''
                - 09 -
    Write a Python program to display the examination schedule. (extract the date
    from exam_st_date).
    exam_st_date = (11, 12, 2014)
    Sample Output : The examination will start from : 11 / 12 / 2014
    '''



    '''
                - 10 -
    Write a Python program that accept an integer (n) and computes the value of
    n+nn+nnn.
    Sample value of n is 5 
    Expected Result : 615
    '''



    '''
                - 11 -
    Write a Python program to print the documents (syntax, description etc.) of
    Python built-in function(s). 
    Sample function : abs()
    Expected Result : 
    abs(number) -> number
    Return the absolute value of the argument.
    '''



    '''
                - 12 -
    Write a Python program to print the calendar of a given month and year.
    Note : Use 'calendar' module. 
    '''



    '''
                - 13 -
    Write a Python program to print the following here document.
    Sample string :
    a string that you "don't" have to escape
    This
    is a ....... multi-line
    heredoc string --------> example
    '''



    '''
                - 14 -
    Write a Python program to calculate number of days between two dates.
    Sample dates : (2014, 7, 2), (2014, 7, 11)
    Expected output : 9 days 
    '''



    '''
                - 15 -
    Write a Python program to get the volume of a sphere with radius 6.
    '''



    '''
                - 16 -
    Write a Python program to get the difference between a given number and 17, 
    if the number is greater than 17 return double the absolute difference.
    '''



    '''
                - 17 -
    Write a Python program to test whether a number is within 100 of 1000 or 2000.
    '''



    '''
                - 18 -
    Write a Python program to calculate the sum of three given numbers, if the
    values are equal then return thrice of their sum.
    '''



    '''
                - 19 -
    Write a Python program to get a new string from a given string where "Is"
    has been added to the front. If the given string already begins with "Is"
    then return the string unchanged. 
    '''



    '''
                - 20 -
    Write a Python program to get a string which is n (non-negative integer)
    copies of a given string.
    '''



    '''
                - 21 -
    Write a Python program to find whether a given number (accept from the user)
    is even or odd, print out an appropriate message to the user.
    '''



    '''
                - 22 -
    Write a Python program to count the number 4 in a given list.
    '''



    '''
                - 23 -
    Write a Python program to get the n (non-negative integer) copies of the
    first 2 characters of a given sting. Return the n copies of the whole string
    if the length is less than 2.
    '''



    '''
                - 24 -
    Write a Python program to test whether a passed letter is a vowel or not.
    '''



    '''
                - 25 -
    Write a Python program to check whether a specified value is contained in a
    group of values.
    Test Data : 
    3 -> [1, 5, 8, 3] : True
    -1 -> [1, 5, 8, 3] : False
    '''



    '''
                - 26 -
    Write a Python program to create a histogram from a given list of integers.
    '''



    '''
                - 27 -
    Write a Python program to concatenate all elements in a list into a string 
    and return it.
    '''



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



    '''
                - 30 -
    Write a Python program that will accept the base and height of a triangle
    and compute the area.
    '''



    '''
                - 31 -
    Write a Python program to compute the greatest common divisor (GCD) of two
    positive integers.
    '''



    '''
                - 32 -
    Write a Python program to get the least common multiple (LCM) of two positive
    integers.
    '''



    '''
                - 33 -
    Write a Python program to sum of three given integers. However, if two values
    are equal sum will be zero.
    '''



    '''
                - 34 -
    Write a Python program to sum of two given integers. However if the sum is
    between 15 to 20 it will return 20.
    '''



    '''
                - 35 -
    Write a Python program that will return true if the two given integer values
    are equal or their sum or difference is 5.
    '''



    '''
                - 36 -
    Write a Python program to add two objects if both objects are integer type.
    '''



    '''
                - 37 -
    Write a Python program to display your details like name, age, address in
    three different lines.
    '''



    '''
                - 38 -
    Write a Python program to solve (x + y) * (x + y).
    Test Data : x = 4, y = 3
    Expected Output : (4 + 3) ^ 2) = 49
    '''



    '''
                - 39 -
    Write a Python program to compute the future value of a specified principal 
    amount, rate of interest, and number of years.
    Test Data : amt = 10000, int = 3.5, years = 7
    Expected Output : 12722.79
    '''



    '''
                - 40 -
    Write a Python program to compute the distance between the points (x1, y1)
    and (x2, y2).
    '''



    '''
                - 41 -
    Write a Python program to check whether a file exists.
    '''



    '''
                - 42 -
    Write a Python program to determine if a Python shell is executing in 32bit
    or 64bit mode on OS.
    '''



    '''
                - 43 -
    Write a Python program to get OS name, platform and release information.
    '''



    '''
                - 44 -
    Write a Python program to locate Python site-packages.
    '''



    '''
                - 45 -
    Write a python program to call an external command in Python.
    '''



    '''
                - 46 -
    Write a python program to get the path and name of the file that is currently 
    executing.
    '''



    '''
                - 47 -
    Write a Python program to find out the number of CPUs using.
    '''



    '''
                - 48 -
    Write a Python program to parse a string to Float or Integer.
    '''



    '''
                - 49 -
    Write a Python program to list all files of a directory in Python.
    '''



    '''
                - 50 -
    Write a Python program to print without newline or space.
    '''



    '''
                - 51 -
    Write a Python program to determine profiling of Python programs.
    Note: A profile is a set of statistics that describes how often and for how 
    long various parts of the program executed. These statistics can be formatted 
    into reports via the pstats module.
    '''



    '''
                - 52 -
    Write a Python program to print to stderr.
    '''



    '''
                - 53 -
    Write a python program to access environment variables.
    '''



    '''
                - 54 -
    Write a Python program to get the current username.
    '''



    '''
                - 55 -
    Write a Python to find local IP addresses using Python's stdlib.
    '''



    '''
                - 56 -
    Write a Python program to get height and width of console window.
    '''


if __name__ == "__main__":
    basicPythonExercises()