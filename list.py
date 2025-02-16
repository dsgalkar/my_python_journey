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