## es 2: Print the sum of the current number and the previous number
i = 0
prev = 0
sum = 0
for i in range (10):
    sum = i + prev
    prev = i
    print("Current Number %s Previous Number %s Sum: %s" % (i, prev, sum))
