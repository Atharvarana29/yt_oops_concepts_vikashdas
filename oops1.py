# initiating a class 

class employee:
    # assigning data and attributes to this class => this method is called 
    # special methods / magic method / dunder methods - the method used to define the data and attribute is called constructor 
    # how to make a constructor?

    def __init__(self):
        # defining the attributes or data that this employee class will have 
        print("started executing attributes/data")
        self.id =  123
        self.salary = 5000 
        self.designation = "SDE"
        # object bante hi ye sare attributes call ho jate hai but functions nahi 
        print("attributes/data have been initiated")

        # whenever we define a method inside a class then it is called a function 
        # difference between method and function 

    def travel(self , destination):
        print("this travel method was called manually")
        print(f"employee is now travelling to {destination}")



# now we will create an object of this employee class
# creating an object/instance of the class
# we cannot create the object of this class by being inside the class
sam = employee()

# now wherever we will call this object sam which is an object of employee class then we will get all the attributes associated with it 
# wherever we will call the object sam we will get all its attributes which ever we want 

# attributes gets called by self automatically as soon as we make the object but the methods or the functions does not gets called by self 
# the functions need to be manually called 

# print(sam.id)
# print(sam.salary)
# print(sam.designation)

# calling a method 
# now we will be accessing our methods 
sam.travel("kerala")

#### so we can say that the real use of constructor is that when ever we call any object of the class then it should automatically call all its attributes 
# eg : whenever we open insta then atuomatically it gets connected to internet , cloud and other , it does not asks user to try and make the app connect to internet and cloud
# these all happens because all those functionalities are being defined inside the constructor attribute and not defined as the methods which need to specifically called . 

print(type(sam))