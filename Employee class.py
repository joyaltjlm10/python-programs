class Employee:
    def __init__(self,name,id,bs):
        self.name=name
        self.id=id
        self.bs=bs
        self.hra = 0
        self.pf = 0
        self.net = 0
        self.da=0
    def display(self):
        print("EMPLOYEE DETAILS")
        print("---------------")
        print("Employee Name : ", self.name)
        print("Employee ID : ", self.id)
        self.hra=(self.bs*10)/100
        self.pf=(self.bs*12)/100
        self.da=(self.bs*5)/100
        self.net=(self.bs+self.hra+self.da)-self.pf
        print("HRA:",self.hra)
        print("PF:",self.pf)
        print("DA:", self.da)
        print("Net Salary:",self.net)
while(1):
    print("1.EMPLOYEE DETAILS\n2.EXIT")
    c=int(input("Enter the choice"))
    if(c==1):
        name=input("Enter the name of the Employee")
        id=int(input("Enter the Employee Id"))
        bs=int(input("Enter the Base Salary"))
        em=Employee(name,id,bs)
        em.display()
    elif(c==2):
        print("Thank YOU")
        exit()