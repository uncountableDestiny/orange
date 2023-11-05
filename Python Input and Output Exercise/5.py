# 5: Accept a list of 5 float numbers as an input from the user
# Expected Output:

# [78.6, 78.6, 85.3, 1.2, 3.5]

floatstring = list((input("Insert 5 float number separate by space: ").split()))
floatlist = list(float(i) for i in floatstring)
print(floatlist)