

######

# Polymorphism     : one functionality with different behaviours


### the ability to appears in more than one form


overriding :
    
    
class parent:
    def mrg: black
    
class child(parent):
    def mrg : red
    

#######################
ex 1:   overriding variables
    
    # if we are overriding then our class variable executed
    
    
class parent:
    name = "ratan"
    
class child(parent):
    name = "anu"
    
c = child()
print(c.name)

##############


    # if we are not overriding then parent class variable executed
    
    
class parent:
    name = "ratan"
    
class child(parent):
    pass
    
c = child()
print(c.name)



##################################

ex 2 :   overriding methods




case 1
# if we are overriding method then our class method executed

class parent:
    def mrg(self):
        print("black grl")
        
class child(parent):
    def mrg(self):
        print("red grl")
        
c = child()
c.mrg()     






case 2

# if we are not overriding then parent class method executed

class parent:
    def mrg(self):
        print("black grl")
        
class child(parent):
    pass
        
c = child()
c.mrg()     



####################################################

ex 3

class parrot:
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("parrot can't swim")
        
class penguin:
    def fly(self):
        print("penguin can't fly")
        
    def swim(self):
        print("penguin can swim")
        

# common interface
def flying_test(bird):
    bird.fly()
    
# creat the objects
pa = parrot()
pen = penguin()

# passing the objects
flying_test(pa)
flying_test(pen)
        

######################################

ex 4



class unicorn():
    def speed(self):
        print("unicorn speed 150kmph")
        
class splender:
    def speed(self):
        print("splender speed 100kmph")
        
#common data

def speed_test(sp):
    sp.speed()
    
#creat the objects
u = unicorn()
s = splender()

# pass the objects

speed_test(u)
speed_test(s)



# at run time which object we are passing that method will be exicuted




