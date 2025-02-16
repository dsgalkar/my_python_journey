# Write your code
print("\n")   
print("type1")   
LL=16
UP=30
for num in range (LL,UP+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:               
                break
        else :
            print (num)   
            
            
            
print("\n")
print("\n")   
print("type2")   
        
lower = 17
upper = 30
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       print("for :2 -",num)
       for i in range(2, num):
           print("Num :", num,", i :", i)
           if (num % i) == 0:
               print('Break !!!\n')
               break
       else:
           print("!! Prime No !!")
           print(num)

    
    
    
    
print("\n")   
print("type3")   
lower = int(input("enter lower number : "))
upper =int(input("enter upper number:"))   
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       print("for :2 -",num)
       for i in range(2, num):
           print("Num :", num,", i :", i)
           if (num % i) == 0:
               print('Break !!!\n')
               break
       else:
           print("!! Prime No !!")
           print(num)

print("\n")   
    
print("\n")   
print("type4")   
 
    
    
    
    

lower = int(input("enter lower number : "))
upper =int(input("enter upper number:"))   
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       print("for :2 -",num)
       for i in range(2, num):
           print("Num :", num,", i :", i)
           if (num % i) == 0:
               print('Break !!!\n')
               break
       else:
           print("!! Prime No !!")
           print(num)      
    
print("\n")   
print("type5")