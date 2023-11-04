""" Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers """
def check_palindrome(numb):
    str_num = str(numb)
    if str_num == str_num[::-1]:
        return True
    else:
        return False
    
print(check_palindrome(4447444))
print(check_palindrome(44432423))