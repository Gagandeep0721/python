# Question 1:
# Write a function to print “hello_USERNAME!” USERNAME is the input of the function. The first line of the code has been defined as below.
from numbers import Number


def hello_name(user_name):
 
  # My answer
 hello_name= input('world')  
print("Hello, " + "world".title() + "!")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
#def first_odds():

#my answer
def first_odds():
  numbers = list(range(0, 101))
  for number in numbers:
     if number %2 != 0:
        print(number)


      
 
  
  #Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below
#def max_num_in_list(a_list):

def max_num_in_list(a_list):
   max_num = max(a_list)
   return max_num
test = max_num_in_list([2,3,5,8,9])
print(max_num_in_list ([2,3,5,8,9]))
 



# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).


def is_leap_year(a_year):
        if a_year % 4 == 0 (a_year % 400 == 0 or a_year % 100 != 0):
          print(True)
        else:
          print(False)
is_leap_year(2019)
  

   
   
   #Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
# def is_consecutive(a_list)

# answer
def is_consecutive(a_list):
   i = 0
   status = True
   while i < len(a_list) - 1:
      if a_list[1] + 1 ==a_list[i + 1]:
         i += 1
      else:
         status = False
         break
      print(status)
   
   
     
   
   
   

