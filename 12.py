""" 
Exercise 12: Calculate income tax for the given income by adhering to the rules below
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:

For example, suppose the taxable income is 45000, and the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000. """

def taxIncome(income):
    if (income<=10000):
        print ("%s*0% = 0" % (income))
    elif (income<=20000):
        remaining = income - 10000
        res = remaining *0.1
        print ("10000*0% + \%s*10% = %s" % (remaining, res))
    else:
        remaining = income - 20000
        res = remaining * 0.2 + 10000 * 0.1
        print ("10000*0% + 10000*10% + " + str(remaining)+"*20% = $" + str(res))

taxIncome(45000)