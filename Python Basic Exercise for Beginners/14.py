""" 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
* * * * *  
* * * *  
* * *  
* *  
* """
num = 5
char = "* "
for y in range(num, 0, -1):
    line = char
    for x in range (y-1):
        line += char
    print(line)
    
