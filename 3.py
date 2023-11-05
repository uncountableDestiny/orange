#Exercise 3: Print characters from a string that are present at an even index number
s = input("Orginal String is ")  
for i in range(len(s)):
    if i%2 == 0: print(s[i])