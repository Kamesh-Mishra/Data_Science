

class Myclass:
    pass

class Myclass2():
    pass

class Myclass3(object):
    pass

print(issubclass(Myclass, object))

print(issubclass(Myclass2, object))

print(issubclass(Myclass3, object))


#################################

# declaring function inside the class


class mycls:
    def disp1(self):
        print('good morning')
        
    def disp2(self,name):
        print("good morning",name)
        
        
        
c = mycls()

c.disp1()
c.disp2("ratan")



################################

#instance and static method






class Myclass:
    def m1(self):
        print("instance method")
        
        
    @staticmethod
    def m2():
        print("static method")
        
        
c = Myclass()
c.m1()


Myclass.m2()
    
##################################

# declaring variables inside the class 

#         to represent class variable inside the class use :  self
#         to represent class variable outside the class use :  object-name



class myclass():
    a,b = 10,20
    
    def add(self):
        print(self.a+self.b)
        
    def mul(self):
        print(self.a*self.b)
        
        
c= myclass()
c.add()
c.mul()

print(c.a)
print(c.b)


############################################

# local var , class var , global var     : different names




i,j = 100,200                   # global var
class myclass():
    a,b = 10,20                 # class var
    
    def add(self,x,y):          # local var
        print(x+y)
        print(self.a+self.b)
        print(i+j)
        
        
    def mul(self,x,y):
        print(x*y)
        print(self.a*self.b)
        print(i+j)
        
c= myclass()
c.add(2,2)
c.mul(3,3)


########################################################

# local var , class var  , global var  :  same name

a,b = 100,200                       # global var
class myclass():
    a,b = 10,20                     # class var
    
    def add(self,a,b):               # local var
        
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b'])
        
    def mul(self,a,b):
        print(a*b)
        print(self.a*self.b)
        print(globals()['a']*globals()['b'])
        
c = myclass()
c.add(2,2)
c.mul(3,3)
 



#################################################################



# for a single class we can creat multiple objects

class myclass:
    def disp(self):
        print("good morning")


c1 = myclass()
c1.disp()

c2 = myclass()
c2.disp()





####################################################


# OBJECT CREATION FORMATS   : 2 FORMATS

#  named object            : c1 = myclass()   : object with reference
# name less object         : myclass()        : object without refernce

class myclass:
    def disp(self):
        print("good morning")



# named object
        
c1 = myclass()
c1.disp()


# name less object

myclass().disp()


################################################################

#     id()   : to print memory addr

#     is  , is not  : memory comparison

class myclass():
    pass

c1 = myclass()
c2 = myclass()
c3 = c1


print(id(c1))
print(id(c2))
print(id(c3))




print(c1 is c2)
print(c1 is c3)


print(c1 is not c2)

print(c1 is not c3)


############################################################

# modification in particular object remains for only that particular object only others do not effects




class myclass:
    name = "ratan"

c1 = myclass()
print(c1.name)      #ratan

c1.name = "anu"
print(c1.name)      #anu


c2 = myclass()
print(c2.name)      #ratan





