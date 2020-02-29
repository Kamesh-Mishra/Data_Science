

# declaring constructor inside the class  :   __init__()



class myclass():
    def m1(self):
        print("good morning")
        
    def __init__(self):
        print("0-arg constructor")
        
c = myclass()

c.m1()

# constructor logics are automatically exicuted when we creat the objects

#   methods are exicuted when we call the methods





##############################################


class myclass:
    
    def values(self,val1,val2):    # local var
    
        print(val1)
        print(val2)
        
        #conversion of local var to class-var
        
        self.val1 = val1
        self.val2 = val2
    
    def add(self):
        print(self.val1+self.val2)
        
    def mul(self):
        print(self.val1*self.val2)
        
c = myclass()
c.values(3,3)

c.add()
c.mul()

    
        

########################################################

class myclass:
    def m1(self):
        print("m1 method")
        self.m2(10)               #calling current class method
        
    def m2(self,a):
        print("m2 method:",a)
        
c= myclass()
c.m1()
        
        
        
        
##############################################################

 
   
class myclass:
    name = "durga"
    def __init__(self,name):
        print("good morning",name)
        print("good evening",self.name)
        
c = myclass("ratan")


###############################################################


     
class Operations:
    def __init__(self,val1,val2):
        print(val1)
        print(val2)
        
        #conversion of local var to class var
        
        self.val1 = val1
        self.val2 = val2
        
    def add(self):
        print(self.val1+self.val2)
        
    def mul(self):
        print(self.val1*self.val2)
        
o  = Operations(4, 4)
o.add()
o.mul()





###################################################################




class Emp:
    def __init__(self,eid,ename,esal):
        
        self.eid = eid
        self.ename = ename
        self.esal = esal
        
    def disp(self):
        print(self.eid,self.ename,self.esal)

e = Emp(123,"ratan",12345)


e.disp()


#######################################################

#   __str__  : it will be executed when we print ref-var



#    case 1

class myclass:
    pass

c = myclass()

print(c)


# <__main__.myclass object at 0x000002828B36F708>






# case 2

class myclass:
    def __str__(self):
        return "ratan"
    
c = myclass()
print(c)

# ratan


# case 3 

class myclass:
    def __str__(self):
        return 10
    
c = myclass()
print(c)


  #  TypeError: __str__ returned non-string (type int)              


# case 4 

class myclass:
    def __str__(self):
        print("ratan")
    
c = myclass()
print(c)


# TypeError: __str__ returned non-string (type NoneType)



############################################


class Emp:
    def __init__(self,eid,ename,esal):
        
        self.eid = eid
        self.ename = ename
        self.esal = esal
        
    def __str__(self):
        return  "emp id:{} emp name:{} emp esal:{}".format(self.eid,self.ename,self.esal)

e1 = Emp(123,"ratan",12345)
print(e1)       # printing refrence var : internally it calls __str__


e2 = Emp(222,"anu",200000)
print(e2)




################################################################

 

# __del__   :   executed when we destroy object




class myclass:
    def __del__(self):
        print("object destroyed . . . ")
        
        

c1 = myclass()

c2 = myclass()

del c1
del c2


##########################################




class myclass:
    def __del__(self):
        print("object destroyed . . . ")
        
        

c1 = myclass()
c2 = c1
c3 = c1


del c1
del c2
del c3



# case1 

class myclass():
    def __del__(self):
        print("object destroyed ....")
        print(10/0)
        
c = myclass()

del c


"""
Exception ignored in: <function myclass.__del__ at 0x000002828C367048>
Traceback (most recent call last):
  File "<ipython-input-96-acd386d92bda>", line 4, in __del__
ZeroDivisionError: division by zero
"""

