o=[]
e=[]
a=int(input("Enter the no.of elements in the 1st list : "))
print("Enter the elements : ")
for i in range (a) :
    b=int(input())
    o.append(b)
c=int(input("Enter the no.of elements in the 2nd list : "))
print("Enter the elements : ")
for i in range (c) :
    d=int(input())
    e.append(d)
o.extend(e)
e.clear()
for i in o :
    if (i%2==0) :
        e.append(i)
        o.remove(i)
print("ODD NUMBERS LIST : \n",o)
print("EVEN NUMBERS LIST : \n",e)