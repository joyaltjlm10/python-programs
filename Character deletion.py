a=input("Enter the String : ")
b=input("Enter Character to be deleted : ")
c=""
for i in a :
    if (i==b) :
        continue
    else :
        c=c+i
print (c)
