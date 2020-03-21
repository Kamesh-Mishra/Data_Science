



  # Abstraction

# ex 1 

from abc import ABC, abstractmethod

class A(ABC):
    
    @abstractmethod
    
    def disp(self):
        pass
    
class B(A):
    
    def disp(self):
        print("good morning")
        
        
b = B()
b.disp()


####################


from abc import ABC, abstractmethod

class A(ABC):
    
    @abstractmethod
    
    def disp(self):
        pass
    
class B(A):
    
    def disp(self):
        print("good morning")
        
b = B()
b.disp()

a = A()     #TypeError: Can't instantiate abstract class A with abstract methods disp

###############################################


# ex 2

from abc import ABC,abstractmethod

class person(ABC):
    def eat(self):
        pass

class ratan(person):
    def eat(self):
        print("5-idly")
        
class durga(person):
    def eat(self):
        print("4-idly")
        
r = ratan()
r.eat()

d = durga()
d.eat()





#############################

from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def disp1(self):
        pass
    
    @abstractmethod
    def disp2(self):
        pass
    
class ratan(A):
    def disp1(self):
        print("good morning")


r = ratan()

# TypeError: Can't instantiate abstract class ratan with abstract methods disp2


#################


from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def disp1(self):
        pass
    
    @abstractmethod
    def disp2(self):
        pass
    
class ratan(A):
    def disp1(self):
        print("good morning")

class anu(ratan):
    def disp2(self):
        print("good morning")
        
a = anu()
a.disp1()
a.disp2()


r = ratan()  #TypeError: Can't instantiate abstract class ratan with abstract methods disp2




###################################################

# ex 4



from abc import ABC,abstractmethod

class A(ABC):
    
    def __init__(self,value):               #local var
        self.value = value
        

    @abstractmethod 
    def disp(self):
        pass
        
class add(A):
    def disp(self):
        print(10+self.value)
        
class mul(A):
    def disp(self):
        print(10*self.value)
        
a = add(10)
b = mul(5)

a.disp()
b.disp()
       
        









#############################################


# ex 5


from abc import ABC,abstractmethod

class A(ABC):
    
    def __init__(self,value):               #local var
        self.value = value
        
    
class add(A):
    def disp(self):
        print(self.value)
        
class mul(A):
    def disp(self):
        print(self.value)
        
a = add(10)
b = mul(5)

a.disp()
b.disp()
       
       