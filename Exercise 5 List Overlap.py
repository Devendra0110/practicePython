# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between
#  the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:
# Randomly generate two lists to test this
# Write this in one line of Python 

import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c =  list(set(a) & set(b))      
print('Common elements: '+str(c))

a = random.sample(range(0,40),10)
b = random.sample(range(0,40),10)
c =  list(set(a) & set(b))
print("list a:"+str(a))
print("list b:"+str(b))
if len(c) > 0:
    print('Common elements: '+str(c))
else:
    print('No common elements in random list')