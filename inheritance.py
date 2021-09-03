class A:
    def feautures1(self):
        print('Features1 is added')
    def feautures2(self):
        print('Features2 is added')

#another child class
class B(A):      #class B inherited class A
    def feautures2(self):
        return super().feautures2()

#object create

a = A()

a.feautures1()
a.feautures2()

b = B()
b.feautures2()