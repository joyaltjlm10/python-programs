a=int(input("Enter the no. of data : "))
v=['a','e','i','o','u']
l=[]
c=[]
s=[]
print ("Enter the datas of the list : ")
for i in range (a) :
  b=input()
  l.append(b)
for i in l :
  if i in v :
      s.append (i)
  else :
      c.append (i)
print ("VOWLeS :",s)
print ("CONSONANTS :",c)
      
