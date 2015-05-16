class MyClass():
    a = 1;

    def fact(self, n):
        if(n==0):
            return 1
        else:
            return n*(self.fact(n-1))


myObject = MyClass()
print myObject.fact(5)

fun = lambda x,y,z : x*y*z
a = [(1,2,3),(2,3,4),(3,4,5)]
b = map(lambda x: x[0]*x[1]*x[2], a)
print b
