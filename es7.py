""" Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string. """

str_x = "Emma is good developer. Emma is a writer"

def countKey(str, keyword):
    count = str.count(keyword)
    print("%s is present %s times" % (keyword, count))
    
countKey(str_x, "Emma")