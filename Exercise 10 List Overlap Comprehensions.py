import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
commonSet = [num for num in set(a) if num in b]  
if len(commonSet) > 0:
    print("Common Set: "+ str(commonSet))
else :
    print("Nothing is commont")

# Randomly generated List

a = random.sample(range(0,90),15)
b = random.sample(range(0,80),10)
commonSet = [num for num in set(b) if num in a]
print("Random List a: "+str(a))
print("Random List b: "+str(b))
if len(commonSet) > 0:
    print("Common Set in random generated list: "+ str(commonSet))
else :
    print("Nothing is commont")
