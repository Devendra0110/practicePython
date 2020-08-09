def getFibonacci(length) :
    series = [1,1]
    head = 1
    tail = 1
    while length > 2 :
        series.append(head + tail)
        pointer = head
        head += tail        
        tail = pointer
        length -= 1
    return series

num = input("How many numbers you want to generate?\n")
print(getFibonacci(int(num)))