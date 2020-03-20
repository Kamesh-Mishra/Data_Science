

# Encapsulation   : the process of binding data  


# private : "__"

# ex 1 : private variables : we can accesss only with in the  class


class A:
    __a = 10
    def disp(self):
        print(self.__a)
        
obj = A()
obj.disp()



print(obj.__a)        # AttributeError: 'A' object has no attribute '__a'



############################################

# ex 2:   private methods



class myclass():
    def __disp1(self):
        print("private method")
        
    def disp2(self):
        print("this is disp2 calling disp1")
        self.__disp1()
        


c = myclass()
c.disp2()

c.__disp1()         # AttributeError: 'myclass' object has no attribute '__disp1'




###########################################

# ex 3:     

    
    
class emp:
    __eid=111
    
    def seteid(self,eid):
        self.__eid = eid
        
    def geteid(self):
        return self.__eid
    
e = emp()

# AttributeError: 'emp' object has no attribute '__eid'

print(e.geteid())        

e.seteid(222)

print(e.geteid())






####################################

# ex 4 : problem : every method creat the object




class A:
    num1,num2 = 100,200
    
class B:
    def add(self):
        a = A()
        print(a.num1+a.num2)
        
    def mul(self):
        a = A()
        print(a.num1*a.num2)
        
b = B()
b.add()
b.mul()


###############################################

# ex 5 :   solution : one time creat the object use multiple times





class A:
    num1,num2 = 100,200
    
class B:
    
    a = A()
    
    def add(self):
        print(self.a.num1+self.a.num2)
        
    def mul(self):
        print(self.a.num1*self.a.num2)
        
b = B()
b.add()
b.mul()












