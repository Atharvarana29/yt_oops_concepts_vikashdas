class chatbook:
    # initialized the constructor 
    def __init__(self): # self -> refers to the newly created instance 
        self.username = ''
        self.password = ''
        self.loggedin = False # initially
        self.menu() # method nniche alag sae bhi bana kae upar yaha par attribute kae taur par bhi call kar sakte hai . jo bhi method ko call karna hai usko yaha likh dena hai 
    # humare constructor kae andar hi yae logic tha ki menu ko call karna hai  

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
