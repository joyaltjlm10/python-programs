class Bank:
    def __init__(self,name,acno):
        self.name=name
        self.acno=acno
        self.bal=0
    def display(self):
        print("ACCOUNT DETAILS")
        print("---------------")
        print("Account Holder : ", self.name)
        print("Account Number : ", self.acno)
    def deposit(self,dm):
        self.dp=dm
        self.bal=self.bal+self.dp
        print(dm,"Deposited succesfully")
    def withdraw(self,wm):
        self.wd=wm
        if self.bal>self.wd:
            self.bal = self.bal - self.wd
            print(self.wd,"withdraw succesfully")
        else:
            print("Insufficent Balance")
    def view(self):
        print("Account Balance:",self.bal)


name=input("Enter the name of the account holder : ")
acno=int(input("Enter the account Number : "))
b=Bank(name,acno)
b.display()
while(1):
    print("1.Deposit Money\n2.Withdraw Money\n3.View Balance\n4.Exit")
    c=int(input("Enter Your Choice"))
    if(c==1):
        dm = int(input("Enter the amount to be deposited"))
        b.deposit(dm)
    elif(c==2):
        wm=int(input("Enter the Amount to withdraw"))
        b.withdraw(wm)
    elif(c==3):
        b.view()
    elif(c==4):
        print("Thank You")
        exit()