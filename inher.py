# this becomes our parent class 
class Animal:
    def __init__(self , name): # constructor call hoga tab hi na tum self ko call kar sakte ho , bcz wo constructor hi hai jo self ko map karne mae help karta hai 
        self.name = name
        self.__name = name # private variable i.e if we hide an attribute (or we can say if we encapsulate an attribute ), then it will not get inherited into the child class ❌ Not exactly.

# It still gets inherited.
# It just gets renamed internally. bcz Python does not have true private variables — only name mangling.
 
    # and there is a function which is using this name attribute 
    def speak(self):
        print(f"{self.name} makes a sound")
        # pass


# now we are going to make a child class 
class Dog(Animal): # as an argument pura ka pura parent class (Animal) de denge.
    # so even though we don't create any attribute in this Dog class but still we can use the attribute of the parent class , bcz those attributes gets inherited here . 
    
    # constructor banayege tabhi self call hoga na 
    def __init__(self,name):
        # self.behaviour = "freindly"  # now since we have made the constructor so it is better to write it inside the super()

    # aur agar hum child class kae andar constructor bana diye hai tho fir hum parent class kae attribute to simply call nahi kar sakte . , this is called constructor overloading 
    # child constructor banae kae baad parent class ka attribute use karne kae liye we need to user super()
    # and also agar child kae pass bhi wo method exist karta hai same naam sae jo parent class mae hai tab wo child class wala hai method use karega . 
        # i.e indirectly we can say that jab child class ko pata hi nahi hota ki life mae kya karna hai then wo parent class ko hi apna attribute maan leta hai and 
        # jab hum child class mae constructor initiliaze kar dete hai i.e jaab child class ko pata hota hai ki usko life mae kya karna hai , tab wo parent class kae attribute ya opinion ko nullify kar deta hai and use nahi karta ya nahi kar sakta .


        # but still if we want that child class use kare parent class ke attributes ko even though constructor has been initialized in the child class then we need to user the super method to initilize the constructor .
        # and similarly if both parent and child class has same function name and we want to  use the parents method then again we have to use the super method here .
        # the super method here gives the priority to the function of the parent class if the names are same else it remians the child class priority. 
        
        #super can be used inside child class only.  
        super().__init__(name) # calling parent constructor
        self.behaviour = "freindly"
    def speak1(self): # so even though we are using the method we can use it according to our use case 
        print(f"{self.name} barks. He is very {self.behaviour}") # here we have not defined behaviour attribute inside our parent class attribute but we can define it in our child class and thus it will not be accessed by our parent class 
    

    
    # difference is that in this child class it does not have any constructor , it just contains a function
# create an instance or you can say an object of the class
animal = Animal("Generic Animal") # because our init is asking for an  argument 
animal.speak() # output : Generic Animal makes a sound 

dog = Dog("Buddy")
# dog = Dog()
dog.speak1() # i.e dog class ko use kar kae uss par aise method ko bhi call kar sakte hai jo uske pass hai hi nahi , i.e jo parent class mae hai  

dog.speak()
# but vice-a-versa is not true
# animal.speak1() 


##### the same hierarchy can be used in real life examples like students studying in the college , will all share the same college and other similar details except branch .
##### so in this case we can just call the college class there , this makes our code much reusable and readable and the much resuable our code is the much high level its value is .