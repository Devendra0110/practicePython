print("Enter a string to check if it's palindrome or not")
givenString = input("-->").lower()
if givenString == givenString[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")
