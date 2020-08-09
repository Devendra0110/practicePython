"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

print("Enter a number to check if it is odd or even")
num = int(input('-->'))

if num%4==0:
    print(str(num)+' modulo 4 is 0.')
elif num%2==0:
    print(str(num)+' is an even number' )
else:
    print(str(num)+' is an odd number' )

print("Enter two number to check if second is evenly divide into first")
num1 = int(input('num1:'))
num2 = int(input('num2:'))

if num1 % num2==0:
    print(str(num1)+ ' is evenly divisble by '+str(num2))
else:
    print(str(num1)+ ' is not evenly divisble by '+str(num2))
