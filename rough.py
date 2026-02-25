
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

user1 = chatbook()
# i.e yaha par class hai nahi but we imported the class from other module where this class was actually built and here we are making an object of it 

##### this is what is called modular coding
