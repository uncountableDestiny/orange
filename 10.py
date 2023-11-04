""" Exercise 10: Create a new list from two list using the following condition
Create a new list from two list using the following condition

Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

Given:

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90] 

Expected Output:

result list: [25, 35, 40, 60, 90]
"""

def get_new_list(l1, l2):
    res = []
    for n in l1:
        if n % 2 == 1: 
            res.append(n)
    for n in l2:
        if n % 2 == 0: 
            res.append(n)
    res.sort() # sort the list
    return res

l1 = [10, 23, 25, 60, 120, 74, 88, 52]
l2 = [40, 13, 22, 28, 45, 60, 89, 75, 1100, 90]    
res = get_new_list(l1, l2)
print(res)