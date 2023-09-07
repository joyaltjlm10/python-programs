try :
    a=int(input("Enter the number : "))
    if (a%2==0) :
        print (a,"is an even number !!!")
    else :
        print(a, "is an even number !!!")
except ValueError :
    raise ValueError("Invalid input.Enter a valid integer !!!")
finally :
    print ("Hiii !!!")