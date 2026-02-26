
# # creating objects of their classes 
# lst = [1,2,3]
# my_Str = "mlops playlist"
# my_int = 155

# print(type(lst))
# print(type(my_Str))
# print(type(my_int))

# # everything , every datatype in python is a class 
# # we can also verify it using the attributes 

# # ends_with = my_Str.capitalize()
# # print(ends_with)

# # using method of str class into list 
# list_c = lst.capitalize()
# print(list_c) # this will show error bz capitalize is an attribute of string class not list class 

# #so we can say that in python what ever  data structure or data type(list , str etc ... ) that we see in python are all basically a class developed by developers 

# # i.e in python everything is object so we say python is an oops language 


## testing the modularity of the file 
##### this is what is called modular coding
from oops_proj import chatbook 

# similarly train_test_split is also a class which is written using oops concepts 
# now once we have imported it we can also create an object of it 

# user1 = chatbook()
# i.e yaha par class hai nahi but we imported the class from other module where this class was actually built and here we are making an object of it 

##### this is what is called modular coding


# function vs method 
# lst = [1,2,3]
# # function
# a1 = len(lst)
# print(a1)


# method  => object ko pakad  kae uske upar methods ko access kar sakne kae liyae  
# chatbook class ka user1 object and uska method call karrna cha rahe hai
user1 = chatbook()
# user1.message_Friend()
# print(user1.__name)


# getter and setter in python
user1  = chatbook()
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())

print(user1.id)
# if we use simple attribute : fir sae initialize ho kae fir sae 0 par hi set ho gaya 
# but if we use static attribute then the increament is continious 

# using direct method directly from the class rather than from the object , bcz static method can be directly accesed from the class name
chatbook.set_id(10) #it is like 2 and 10 kae bich mae 9 aur user aaye thae but unka account suspend ho gaya , so now i am entering in between and manually setting its id to 10
# static method use karo  ki aab yaha sae counting suru karo 
user2 = chatbook()
print(user2.id)

# and similiarly abb yah sae sequential counting hoga 
user3 = chatbook()
print(user3.id) 


# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)


# user4 = chatbook()
# print(user4.id)

