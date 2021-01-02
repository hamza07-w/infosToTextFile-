tagain = "try again !"
firstName=input("enter first name : ")
i=0
while  len(firstName)<=2 and i<=3 or len(firstName)>12 and i<=3:
    print("first name to short or long !")
    print(tagain)
    firstName=input("enter first name : ")
	
lastName=input("enter last name : ")
age1=int(input("enter born year : "))
while  not(1900<=age1<2020) :
    print("enter year betwen 1900 -- 2020")
    print(tagain)
    age1=int(input("enter born year : "))
age2=int(input("enter born month : "))
while  not(0<age2<=12):
    print("enter a month betwen 01 -- 12 like 04")
    print(tagain)
    age2=int(input("enter born month : "))
age3=int(input("enter born day : "))
while  not(0<age3<=32):
    print("enter a day betwen 01 -- 32 like 09")
    print(tagain)
    age3=int(input("enter born day : "))
phone_num=input("enter phone number : ")
while  not(15>=len(phone_num)>=10):
    print("phone nember long must be between 0 and 15 nember !")
    print(tagain)
    phone_num=input("enter phone nember : ")
city = input("enter the city : ")


with open(firstName+".txt" , "w") as file:
     f=file.write( "full name is {} {}\nage is{}/{}/{} \nthe city is {}\nphone nember is {} ".format(firstName.upper(),lastName,age1,age2,age3,city.upper(),phone_num))



print("select option to do to the text: ")
print("1.read \n2.append ")
option = input("$~"+firstName+"@root : ")
a=0
while a <= 1:
  if option== "1" or option=="read":
      file=open(firstName+".txt" , 'r') 
      f=file.read()
      print(f)
      a=a+1
  elif option=="2" or option=="append":
  	file=open(firstName+".txt" , 'a')
  	f=file.write(input("add any thing : "))
  	break
  elif option=="3" or option=="exit":
  	break
  	a=a+1
  
	