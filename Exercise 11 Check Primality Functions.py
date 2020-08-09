def isPrime(num) :
    if num == 1 :return False
    divisibles = [i for i in range(1,int(num/2)+1) if num%i==0]
    return len(divisibles) == 1

num = int(input("Enter the number\n->"))

if isPrime(num):
    print(str(num) + " is a prime number")
else:
    print(str(num) + " is not a prime number")
