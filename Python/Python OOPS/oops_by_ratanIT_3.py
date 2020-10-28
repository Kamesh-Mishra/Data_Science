

"""
class        vs          object

1 class is a logical entity represents logics ,,,,   object is a physical entity representing memoryview


2 class is a blue print

3 one class possible to creat multiple objects

4 class keyword declare to class

 

 

main building blocks of oops :
    
    1. Inheritance
    2. Polymorphism
    3. Encapsulation
    4. Abstraction
  """  



"""
1. inheritance :
    
    the process of acquiring the properties of parent class to child class 
    
     the process of creating  new class by using the properties of existing class
     

"""

# inheritance



class parent():
    def m1 (self):
        print("parent m1() method")
        
class child(parent):
    def m2(self):
        print("m2 method")
        
p = parent()
p.m1()

c = child()
c.m1()
c.m2()


######################################


#  calling super class methods  : by using super()




class parent():
    def m1 (self):
        print("parent m1() method")
        
class child(parent):
    def m2(self):
        super().m1()
        print("m2 method")

c = child()
c.m2()




#############################################

# super class variables


class parent():
    a,b = 10,20
    
class child(parent):
    x,y = 100,200
    def add (self,i,j):
        print(i+j)
        print(self.x+self.y)
        print(self.a+self.b)     # accesing parent class variables using self
        
        
c = child()
c.add(1000,2000)


###########################################################



# variables with the same name





class parent():
    a,b = 10,20
    
class child(parent):
    a,b = 100,200
    def add (self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(super().a+super().b)     # accesing parent class variables using super
        
        
c = child()
c.add(1000,2000)



##############################################


# all variables with same name

a,b = 1,2

class parent():
    a,b = 10,20
    
class child(parent):
    a,b = 100,200
    def add (self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(super().a+super().b)     # accesing parent class variables using super
        print(globals()['a']+globals()['b'])      # accesing global variables using       globals()['variable name']  
        
        
c = child()
c.add(1000,2000)




print(issubclass(child, parent))        # checking   child class or not



################################################



 # parent class constructor
 


# case 1

class parent:
    def __init__(self):
        print("parent class constructor")

class child(parent):
    pass

c= child()




# case 2



class parent:
    def __init__(self):
        print("parent class constructor")

class child(parent):
    def __init__(self):
        print("child class cons")


c= child()




# case 3


class parent:
    def __init__(self,name):
        print("parent class constructor :",name)

class child(parent):
    def __init__(self):
        super().__init__("ratan")
        print("child class cons")
        
        

c= child()


# we can call parent class constructor multiple times


class parent:
    def __init__(self,name):
        print("parent class constructor :",name)

class child(parent):
    def __init__(self):
        super().__init__("ratan")
        super().__init__("anu")
        print("child class cons")
        
c= child()






 # another way to access parent class cons
 

class parent:
    def __init__(self,name):
        print("perent class cons",name)
        
class child(parent):
    def __init__(self):

        super().__init__("ratan")

        parent.__init__(self,"anu")

        print("child class cons")
        
c = child()




##############################################################


types of inheritance :
    
    1. single    # one parent class contains one child class
    
    2. multilevel inheritance        # level by lavel
    
    3. multiple inheritance          # one child class : with multiple parent classes
    
    4. hierarcchical inheritance    # one father with multiple childs  

    5. hybrid inheritance     # combination of multiple plus hierarchical inheritance












# 1 single inheritance


class parent:
    pass

class child(parent):
    pass



# 2. multilevel inheritance 
    

class A:           # grand father
    pass 
class B(A):         # father 
    pass
class C(B):          # child
    pass


# 3. multiple inheritance :
    
class A:
    pass
 
class B:
    pass
class C(A,B):                    # multiple fahter and one child
    pass



# 4. hierarcchical inheritance 
    
class A:
    pass
class B(A):
    pass
class C(A):
    pass




################################################
    

# multilevel inheritance
    
class A:
    def m1(self):
        print("m1 method")
        
class B(A):
    def m2(self):
        print("m2 method")

class C(B):
    def m3(self):
        print("m3 method")

c = C()
c.m1()
c.m2()
c.m3()



# we can call parent class methods using child class object

#######################################################



# . hierarcchical inheritance 
   


class vehicle:
    def disp1(self):
        print("vehicle info")
        
class car(vehicle):
    def disp2(self):
        print("car info")
        
class plane(vehicle):
    def disp3(self):
        print("plane info")
        
v = vehicle()
v.disp1()

c = car()
c.disp2()

p = plane()
p.disp3()


#########################################

# multiple inheritance




class parent1:
    def m1(self):
        print("parent1 m1 method")
        
class parent2:
    def m2(self):
        print("parent m2 method")
        
class child(parent1,parent2):
    def m3(self):
        print("child m3 method")
        
c = child()
c.m1()
c.m2()
c.m3()



####################################################


class person:
    def __init__(self,first,last):      # local var
        self.first = first
        self.last = last
        
class emp(person):
    def __init__(self,first,last,id):     # local var
        
        super().__init__(first,last)
        person.__init__(self,first,last)
        self.id = id
        
    def disp(self):
        print("Emp id = {} Emp firstname = {} Emp lastname = {}".format(self.id,self.first,self.last))


e1 = emp("ratan","adddanki",111)
e1.disp()

e2 = emp("anu","s",222)
e2.disp()



# case 1




class person:
    def __init__(self,first,last):      # local var
        self.first = first
        self.last = last
        
class emp(person):
    def __init__(self,first,last,id):     # local var
        
        super().__init__(first,last)
        person.__init__(self,first,last)
        self.id = id
        
    def __str__(self):
        return ("Emp id = {} Emp firstname = {} Emp lastname = {}".format(self.id,self.first,self.last))


e1 = emp("ratan","adddanki",111)
print(e1)

e2 = emp("anu","s",222)
print(e2)

 




###################################################

class parent:
    pass

class child(parent):
    pass

p = parent()
c = child()

print(isinstance(p, parent))

print(isinstance(c, child))

print(isinstance(c, parent))

print(isinstance(c, object))

print(isinstance(p, object))

print(isinstance(p, child))




########################################################










