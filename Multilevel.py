class School :
    def open(self) :
        print ("School Open !!!")
class Classes(School) :
    def started(self) :
        print("Classes started !!!")
class Student(Classes) :
    def present(self) :
        print ("The Student is Present !!!")
c=Student()
c.open()
c.started()
c.present()