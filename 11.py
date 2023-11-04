# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

def reverseNumb(num):
    a = str(num)
    rev = a[::-1]
    spaced = ''
    for i in rev:
        spaced += i + ' '
    print(spaced)
    
    
reverseNumb(345672)