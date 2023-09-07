class Add() :
    def sum(self,a,b) :
        print("Sum")
        print(a+b)
class Sub() :
    def dif(self,a,b) :
        print("Difference")
        print(a-b)
class Mul() :
    def product(self,a,b) :
        print("Product")
        print(a*b)
class Calculator(Add,Sub,Mul) :
    def quo(self, a, b):
        print("Quotient")
        print(a/b)
c=Calculator()
c.sum(10,2)
c.dif(10,2)
c.product(10,2)
c.quo(10,2)