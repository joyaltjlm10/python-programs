unit=float(input("Enter the units : "))
if (unit<=100) :
    amount = unit * 0.5
elif (unit>100 and unit<=150) :
    amount = (100 * 0.5) + (unit - 100) * 0.75
elif (unit>150 and unit<=200) :
    amount = (100 * 0.5) + (50 * 0.75) + (unit - 150) * 1
else :
    amount = (100 * 0.5) + (50 * 0.75) + (50 * 1) + (unit - 200) * 2
print ("THE BILL AMOUNT IS : ",amount)