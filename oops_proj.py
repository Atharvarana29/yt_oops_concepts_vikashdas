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
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("Enter your email here: ")
        pwd = input("enter your password  here : ")
        self.username = email
        self.password = pwd
        print("you have signed up successfully")
        print("\n")
        self.menu() # ye menu ka line add karna i.e menu method call karna hi show karta hai sabse bada advantage of oops concept and modularity 



obj = chatbook()
        
