'''write a program that takes a string and returns true if it is palindrome, false otherwise'''

variable = input("enter the word : ")

if variable == variable[::-1]:
    print("the entered word {a} is palindrome".format(a=variable))
else:
    print("the entered word {a} is not apalindrome".format(a=variable))
