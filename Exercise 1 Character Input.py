"""
This programs takes two input the name and the age. Figure in which year you'll be 100 years old
It uses two inputs for that the input age and the current year. For getting the current year 
it uses a package called 'datetime'. 
Before printing output it also asks how many times you want to see the output
"""

# the package
import datetime

now = datetime.datetime.now()       

# taking inputs
print("Enter your name and age")
name = input('Name:')
age = int(input('Age :'))

#calculating remaining years for you to be 100yr
remainingYears = 100 - age

print("Enter the no. of times you want to see the output")

messageCount = int(input("-->"))
message = "In "+str(remainingYears + now.year)+" you'll be 100 year old"

# print() provide a special syntax which allow you to print same message as many times you want 
# by using * with no. of times you want to see it.
print(messageCount * (message+"\n"))
