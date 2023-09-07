def sum (n) :
    if (n<=1) :
        return n
    else :
        return n + sum (n-1)
s=sum(5)
print (s)