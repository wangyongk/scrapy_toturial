class A(object):
    def show(self):
        print("base show")

class B(A):
    def show(self):
        print("derived show")


obj=B()
obj.show()

obj.__class__=A
obj.show()