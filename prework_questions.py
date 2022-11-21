#Question 1 - Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_" + user_name.upper())

hello_name("username")

print("\n...\n")

# Question 2 - Write a python function, first_odds 
# that prints the odd numbers from 1-100 
# and returns nothing

def first_odds():
    number = list(range(1, 100, 2))
    print(number)

print(first_odds())


print("\n...\n")
 # Question 3 - Please write a Python function, 
 # max_num_in_list to return the max number 
 # of a given list. The first line of the code 
 # has been defined as below.

def max_num_in_list(a_list):
    print(max(a_list))

a_list = [10, 21, 34, 87, 23, 97, 4, 1004]

print(max_num_in_list(a_list))


print("\n...\n")
#Question 4 - Write a function to return if the given year 
# is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if int(a_year) % 4 == 0:
        print(True)
    elif int(a_year) % 100 != 0 and int(a_year) % 400 == 0:
        print(True)
    else: print(False)  

print(is_leap_year(2103))


print("\n...\n")
# Question 5 - Write a function to check to see if all 
# numbers in list are consecutive numbers. For example, 
# [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are 
# not consecutive numbers. The return should be boolean Type.
# def is_consecutive(a_list):

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

a_list = [3, 4, 5,]
print(is_consecutive(a_list))
