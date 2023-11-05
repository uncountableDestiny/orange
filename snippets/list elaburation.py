inputList = [4,7,11,13,18,20]
#creating a list with square values of only the even numbers
squareList = [var**2 for var in inputList if var%2==0]
print(squareList)
#[16, 324, 400]