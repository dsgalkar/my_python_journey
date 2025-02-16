#pip install phonenumbers

import phonenumbers
from phonenumbers import geocoder
#num=int(input("enter the mobile number :"))
phone_number = phonenumbers.parse("+917294536271")
#phone_number = phonenumbers.parse(num)
print(phone_number)
#print()
print("\nPhone number location:\n")
print(geocoder.description_for_number(phone_number, "en"))


#import phonenumbers
#from phone_numbers1 import geocoder
#phone_number1 = phonenumbers.parse("+918446975775")
##phone_number2 = phonenumbers.parse("+918446975775")
##phone_number3 = phonenumbers.parse("+918446975775")
##phone_number4 = phonenumbers.parse("+918446975775")
##phone_number5 = phonenumbers.parse("+918446975775")
#
#
#print("\n Phone numbers location  :\n")
#print(geocoder.description_for_number(phone_number1,"en"))