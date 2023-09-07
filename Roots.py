import math

a=int(input("Enter the coefficient of x^2 : "))
b=int(input("Enter the coefficient of x : "))
c=int(input("Enter the constant : "))
r=(b**2)-(4*a*c)
sq=math.sqrt(r)
if (r==0) :
    x=-b/(2*a)
    print ("This equation will only have one root !!!\nRoot is : ",x)
elif (r>0) :
    x1=(-b+sq)/(2*a)
    x2=(-b-sq)/(2*a)
    print("This equation will have Two roots !!!\nRoots are : ",x1,"and",x2)
else :
    print("This equation will have Two complex roots !!!")