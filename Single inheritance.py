class School :
    def open(self) :
        print ("School Open !!!")
class Classes(School) :
    def started(self) :
        print("Classes started !!!")
c=Classes()
c.open()
c.started()