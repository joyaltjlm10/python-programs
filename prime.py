n=int(input("Enter the no. of list elements : "))
a=[]
for i in range(0,n):
    elem=int(input());
    a.append(elem)
b=[]
for j in a:
    f=0
    for k in range(1,j+1):
        if(j%k==0):
            f=f+1
    if(f==2):
        b.append(j)
print(b)