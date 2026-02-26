class chatbook:
    # initialized the constructor 

    # making a static method : to make the increament everytime a new object is called 
    __user_id = 1  # static method ko self access nahi kar sakta , usko class access kar sakta hai 

    def __init__(self): # self -> refers to the newly created instance 
        self.__name = "default user " # now if we want to hide or protect this attribute then we can use 
        # but if we want to access this we need to use : user1.__chatbook__name format 
        # self.user_id = 0
        # self.user_id+=1 #i.e we want ki har baar jab bhi new user bane tab uski id +1 hoti jaye 
        # abhi ye upar wala acts like dynamic variable because har baar object call hone par iski value reset ho jaa rahi hai and so we need to use static method i.e static variable 
        self.id = chatbook.__user_id # static variable ko self nahi class access karega 
        chatbook.__user_id+=1
        self.username = ''
        self.password = ''
        self.loggedin = False # initially
        # self.menu() # method nniche alag sae bhi bana kae upar yaha par attribute kae taur par bhi call kar sakte hai . jo bhi method ko call karna hai usko yaha likh dena hai 
    # humare constructor kae andar hi yae logic tha ki menu ko call karna hai  

# making getter and setter for static methods 
# using a decorator : ye batane ka ek tarika hai ki ye ek static method hai
    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod # static method ko self dene ki jarurat hai hi nahi, because self tab dete hai jab humara object usko access kar raha ho 
    # but static method  ko access karne kae liye object ki jarurat hi nahi hai 
    def set_id(val): # directly we can pass the argument , and can directly call it using class name 
        chatbook.__user_id = val
        return chatbook.__user_id

# getter
    def get_name(self):
        return self.__name

# setter
    def set_name(self ,value): # value => jo naya name hum set karna chatae hai 
        self.__name = value

    # defining the main menu method 
    def menu(self):
        user_input = input('''welcome to chatbook !! how would like to proceed ?
                           1. press 1 to signup
                           2. press 2 to signin
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press any other key to exit 
                           ''')
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.message_Friend()
        else:
            exit()

    def signup(self): # self refers to this newly created instance  
        email = input("Enter your email here: ")
        pwd = input("enter your password  here : ")
        self.username = email
        self.password = pwd
        print("you have signed up successfully")
        print("\n")
        self.menu() # ye menu ka line add karna i.e menu method call karna hi show karta hai sabse bada advantage of oops concept and modularity 

    def signin(self):
        # if self.signup == True:  this is not the correct way to check the sign up
        if self.username=='' and self.password == '' :
            print("we donot have any user name and password from your side .\n so please sign up first by pressing 1 in the main menu")
            self.menu()
        else: # i.e when our user has already signed up 
            uname = input("greate to see you back here . please enter your email/username here : ")
            pwd_1 = input("please enter your password here")
            self.username = uname
            self.password = pwd_1

            # now we need to check that if the username and the password given matches to the one given during signin 
            if uname == self.username and pwd_1 == self.password:    
                print("you have signed in successfully\n welcome to you your account ")
                print("\n")
                # now initially we had set self.logged in as false , but now the user has signed in successfully 
                # so we can turn off that 
                self.loggedin = True
            else:
                print("\n please provide the correct credentials")
        print("\n")
        self.menu()


    def my_post(self):
        if self.loggedin == True:    
            post = input("Write your post here : ")
            print("\n")
            print(f"following content has been posted -> {post}")
        else:
            print("\n please log in into your account for posting a message")
        print("\n")
        self.menu()

    def message_Friend(self):
        if self.loggedin == True:    
            friend_name = input("enter the name/email of the freind to message")
            own_mail = input("write your own mail")
            msg = input("write the message that you want to send to your friend ")
            print("\n")
            print(f"following content has been posted -> {msg}")
            



# user1 = chatbook()
        
# using this file as a module  we can import the classes into other module 
