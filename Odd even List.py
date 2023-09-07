def Oddeven () :
    e.extend(o)
    e.sort()
    o.clear()
    for i in e :
        if (i%2==0) :
            e.append (i)
        else :
            o.append (i)
            e.remove (i)
    print ("The even number list : \n",e)
    print ("The odd number list : \n",o)
o=[]
e=[]
a=int(input("Enter the no.of elements in the 1st list : "))
print ("Enter the elements of the 1st list : ")
for i in range (a) :
    b=int(input())
    o.append (b)
c=int(input("Enter the no.of elements in the 2nd list : "))
print ("Enter the elements of the 2nd list : ")
for i in range (c) :
    d=int(input())
    e.append (d)
Oddeven ()