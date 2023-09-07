import time,sys

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
typingPrint("***WELCOME TO CONTACT BOOK***\n")
b=[]
while (1):
    print("1.Add Contact\n2.Display Contact \n3.Edit Contact \n4.Exit")
    typingPrint("Enter Your Choice ")
    n=int(input())
    if(n==1):
        a={
            "Name":input("Please enter Your Name "),
            "Ph.No":int(input("Please enter your Ph.No "))
            }
        b.append(a)
        typingPrint("***Contact saved successfully***")
    elif(n==2):
        print("Contacts in your Contact book are")
        print("------------")
        for i in b:
            x=dict(i)
            for x,y in x.items():
                print(x,"-",y)
            print("------------")
        typingPrint("***END OF CONTACTS***")
    elif(n==3):
        l=[]
        s=0
        g=0
        m=input("Enter the name of the contact that has to be edited")
        for i in b:
            x=dict(i)
            for z,y in x.items():
                if y==m:
                    c=input("What do you want to edit")
                    g=s
                    if z==c:
                        x.update({"Name":input("Enter the new name")})
                    else:
                        x.update({"Ph.No":input("Enter the new Phone no.")})
            s=s+1
            l.append(x)
        b[g]=x
        typingPrint("The contact edited Successfully")
          
    elif(n==4):
        typingPrint("***Thank You***")
        break


