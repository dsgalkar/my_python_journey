print("\n\ntype ")
i=1
while (i <= 10):
    print (i)
    i+=1



print("\n\ntype ")
n=int(input("enter the no. of terms :  "))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
    print("sum of number is",sum)


print("\n\ntype ")
college = 'moze college'
for anyvariable in college:
    print(anyvariable)
print ("\n\n")

print("\n\ntype ")
college = {"moze college"}
for anyvariable in college:
    print(anyvariable)
    
print("\n")
for xxx in range (7,15,5):#third no. is the interval beetween two first no.
    print("printing number",xxx)
print("\n")

print("\n\ntype ")
for xxx in range (2,200,2):#third no. is the interval beetween two first no.
    print("printing number",xxx)
print("\n")


print("\n\ntype ")
x=7
x1 =0
x2 =0

for x1 in range(0,x):
    print(" ")
    for x2 in range(0,x1+1):
        print("*",end = "   ")#for *
        #print(x2,end = "   ")#x2 means no. of terms with 0(0starts)
       # print(x2+1,end = "  ")# in this x2 means no. of terms exept 0(0+1 starts)


print("\n\ntype ")
for x1 in range(1,101):
    #print(4 * x)
   
    for x2 in range(1,11):
        print((x1),"* ",(x2),("="),x1*x2)
    print("\n")


print("\n\ntype ")
CollegeNames= "Vidyapeeth", "College","COEP", "Walchand","MozeColl“, “Star", "Arihant", "Suryadatta", "Vedant", "Star"
print(CollegeNames[0])    # Vidyapeeth
print(CollegeNames[2])    # COEP
print(CollegeNames[4])    # MozeColl
#print(CollegeNames[11])  # ??? (Index out of range)

print(" - - - - - - - - - -  Negative Indexing  - - - - ")

print(CollegeNames[-1])   # Vedant
print(CollegeNames[-3])   # Arihant
print(CollegeNames[-5])   # MozeColl
#print(CollegeNames[-20]) # ??? (Index out of range)


print("\n\ntype ")
t1 = "x", "p" ,"True","z","6.34"
print(t1 [-1])
print(t1 [-2])
print(t1[-3])
print(t1[-4])
#left to right  use 0,2,4
#right to left use -1,-2,-3


print("\n\ntype ")
CN = "Star"
print(" ----------Index----------- ")
print(CN , "appears at",CollegeNames.index(CN), "position in the tuple")

print("-----------len----------------")
print("length(number) of the element in the tuple is   :", len(CollegeNames))

print("----------max----------------")
print("highest(max) of the element in the tuple is   :", max(CollegeNames))

print("-----------min----------------")
print("lowest(min) of the element in the tuple is   :", min(CollegeNames))


print("\n\ntype ")
E =(1,2,3,4)
F=E*5
print(F)


print("\n\ntype ")
CollegeNames= "Vidyapeeth", "College","COEP", "Walchand","MozeColl“, “Star", "Arihant", "Suryadatta", "Vedant", "Star"

#print (CollegeNames)

#print(CollegeNames)
#Count()

#CN = "Star"

#print(CN , "appears", CollegeNames.count(CN), "times in the Tuple")

#CN = "OtherName"

#print(CN , "appears", CollegeNames.count (CN) , "times in the Tuple" )



#print()
print("------------count--------------")

CollegeNames = ("vidyapeeth","college","Coep","walchand","mozeColl","star","vedant")
print(CollegeNames)
CN= "star"
print(CN ,"appears",CollegeNames.count)
print("\n\ntype ")

mylist1=["apple","banana","cherry","pineapple","orange","strawberry","guava","peer","apple"]
print(mylist1,"\n")

for name in mylist1:
    print(name)
print("check the apple is there","apple" in mylist1)
print("check the apple is not there","apple" not in mylist1,"\n")
print("check the apple is there","applex" in mylist1)
print("check the apple is not there","applex" not in mylist1,"\n")
print("\n")
print(mylist1[2],"\n")#counter in list is index starts from 0



#slicing
print(mylist1[3:])#element no. 4 to end
print(mylist1[:3])#start to element no 2
print(mylist1[2:5],"\n","\n")#starts at 3 and ends at 5
print("element 1st  :  ",mylist1[0])
print("element 2nd  :  ",mylist1[1])
print("element 3rd  :  ",mylist1[2])
print("element 4th  :  ",mylist1[3],"\n")

print("element 1st  :  ",mylist1[-1])
print("element 2nd  :  ",mylist1[-2])
print("element 3rd  :  ",mylist1[-3])
print("element 4th  :  ",mylist1[-4],"\n","\n")





mylist2 = [45,4,34,567,32,5,32,57]
print(mylist2,"\n")
print(mylist2[2],"\n")#counter in list is index starts from 0
print(mylist2[3:])#element no. 4 to end
print(mylist2[:3])#start to element no 2
print(mylist2[2:5],"\n")#starts at 3 and ends at 5


print("element 1st  :  ",mylist2[0])
print("element 2nd  :  ",mylist2[1])
print("element 3rd  :  ",mylist2[2])
print("element 4th  :  ",mylist2[3],"\n")

print("element 1st  :  ",mylist2[-1])
print("element 2nd  :  ",mylist2[-2])
print("element 3rd  :  ",mylist2[-3])
print("element 4th  :  ",mylist2[-4])
print("\n")
print("\n")



#deleting list element
del mylist1[2]
del mylist1[4]
print (mylist1)

#del mylist1 
print(mylist1)

print("\n")
print("\n")




print("\n")
print("\n")




print("\n")
print("\n")


print("\n\ntype ")
thisdict={"brand":"ford","model":"mustang","year":"1964"}
print(thisdict)
gooddict={2.5:"x",3.75 : "y", 4.5 : 45,"hi":"hello"}
print(gooddict)
alloweddict={1:"one",2:"two",3:"three",4:"four",5:"five",1:"ONE"}
print(alloweddict)
print("\n")
print("\n")
   
   
#slide92
#key:value
allowedDict = {1:"one",2:"two",3:"three",4:"for",2:"five",1:"ONE"}
print(allowedDict)
allowedDict = {1:"one",2:"two",3:"three",4:"for",2:"five",1:"ONE",2:"eight",1:"twenty20"}
print(allowedDict)


print("\n")
print("\n")
#slide 91
CountriesCap = {"india":"new delhi","pakistan":"karachi","russia":"moscow","france":"paris","germany":"berlin"}
print(CountriesCap)


print("\n")
print("\n")
#slide93
print(thisdict.get("brand"))
print(thisdict.get("year"))
print(thisdict.get("ford"))
print(thisdict.get("mustang"))

print("\n")
print("\n")
for key in thisdict:
    print(key,thisdict[key])
    
for key in CountriesCap:
    print("key :",key,", capital,",CountriesCap[key])

print("\n")
print("\n")
#slide96
print()
for key in thisdict:
    print(key,thisdict[key])
print()
for key in CountriesCap:
    print("key :",key,", Capital :", CountriesCap[key])

print("\n")
print("\n")
#slide 97
CountriesCap["portugal"]="lisbon"
Country_Name ="portugal"
print(CountriesCap[Country_Name])
print("Country & Capital City :", CountriesCap)
CountriesCap["Bangladesh"]="Dhaka"
print("Country & Capital city :", CountriesCap)

print("\n")
print("\n")
print("slide100")
CountriesCap["india"]="mumbai"
print("country & capital city :", CountriesCap)

print("\n")
print("\n")
print("slide101")
print("deleting pakistan")
del(CountriesCap["pakistan"])#deleting one pair of elements 
print("Country & Capital city :", CountriesCap)
print()
print("\ngh")
print("deleting last key")
CountriesCap.popitem()#deleting last pair
print("country & capital city :", CountriesCap)

print("\n")
print("\n")
print("slide105")
print (CountriesCap.keys())
print (CountriesCap.values())

print("\n")
print("\n")


print("\n\ntype ")
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