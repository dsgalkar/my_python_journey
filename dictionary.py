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