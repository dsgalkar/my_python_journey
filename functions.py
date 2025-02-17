print(50)
pass  #do nothing but still run successfully
print(50) 
print()
print ("\n\n")





print("slide10") 
def print_me():
    print("print this")
    return
    
print_me()
print("now outside the function")

print ("\n\n")





print("slide12") 
def my_function(fname):
    print("good morning:",fname)
my_function("rohan")
my_function("anjali")
my_function("sayali")
print ("\n\n")




print("slide14") 
def add(x,y):
    z=x+y
    return z
    
z=add(34,76)
print("the sum of two number is :",z)
print ("\n")
print("slide14") 
def add(x,y):
    z=x+y
    zl=x*y
    return z,zl
    
a,m=add(34,76)
#zl=add(34,76)
print(a,m)
print("the sum of two number is :",z)
