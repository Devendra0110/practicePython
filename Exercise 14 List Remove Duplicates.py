import random
def removeDuplicateUsingSet(inputList):
    return (list(set(inputList)))

def removeDuplicateUsingLoop(list):
    removeDuplicatesList  = []
    for a in list:
        if not a in removeDuplicatesList: 
            removeDuplicatesList.append(a)
    return removeDuplicatesList


a = [0, 12, 11, 17, 10, 2, 16, 6, 8, 11, 17]
print(removeDuplicateUsingSet(a))
print(removeDuplicateUsingLoop(a))