#Exercise 5: Check if the first and last number of a list is the same

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

""" Expected Output:

Given list: [10, 20, 30, 40, 10]
result is True

numbers_y = [75, 65, 35, 75, 30]
result is False """

def same (numb):
    if (numb[-1] == numb[0]):
        print("result is True")
    else:
        print("result is False")

def same2 (numb):
    cond = numb[-1] == numb[0]
    print("result is %s" % (cond))

same(numbers_x)
same(numbers_y)

same2(numbers_x)
same2(numbers_y)
