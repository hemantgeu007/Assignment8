import time
'''Importing time module'''
time_now = time.gmtime()
'''Running time.gmtime function'''
import math
'''Importing math module'''

'''Q1'''
'''What is TimeTuple?'''

'''Many of Python's time functions handle time as a tuple of 9 numbers, as shown below. The above tuple is
    equivalent to struct_time structure. This structure has following attributes −
Index 	    Field 	          Attributes                  Values
1 	    4-digit year 	        tm_year                    2008
2 	    Month                   tm_mon                     1 to 12
3   	Day 	                tm_mday                    1 to 31
4 	    Hour 	                tm_hour                    0 to 23
5    	Minute                  tm_min                     0 to 59
6 	    Second                  tm_sec            	       0 to 61 (60 or 61 are leap-seconds)
7    	Day of Week             tm_wday             	   0 to 6 (0 is Monday)
8 	    Day of year 	        tm_yday                    1 to 366 (Julian day)
9 	    Daylight savings        tm_isdst                   -1, 0, 1, -1 means library determines DST
'''

'''Q2'''
print(time.ctime())
'''Printing Formatted time'''

'''Q3'''
month = time_now.tm_mon
print(month)
'''Printing month from time'''

'''Q4'''
day = time_now.tm_mday
print(day)
'''Printing day from time'''

'''Q5'''
year = time_now.tm_year
'''Getting year from time'''
print(str(day) + '/' + str(month) + '/' + str(year))
'''Printing date in the format DD/MM/YYYY'''

'''Q6'''
print(time.localtime())
'''Printing time from localtime() method'''

'''Q7'''
x = int(input("Enter a number: "))
print(math.factorial(x))
'''Printing factorial of number from user input'''

'''Q8'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(math.gcd(a,b))
'''Printing GCD of two numbers from user input'''

'''Q9'''
import os
'''Importing os module'''
print(os.getcwd())
'''Printing Current Working Directory'''
print(os.environ)
'''Printing User Environment'''