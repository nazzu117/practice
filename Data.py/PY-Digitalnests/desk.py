
x="Hyderabad"
print(x)
print(type(x))
print(id(x))
print(x.upper())
print(x.lower())
print(x.capitalize()) # First letter capital
y="good morning hyderabad"
print(y.title()) ## All words first letter makes captals
names="ramu siva ramesh suresh venkat"
print(names.title())
## swapcase():For converting one case to another case if upper it will convert to lower ,if lower makes upper
s="HaPPY Birth day"
w="Java is easy and Java is simple"
print(s.swapcase())
print(s.replace("Birth","Marrage"))
print(s.replace("Birth","Barrage"))  ## replace(): will replace 
print(w.replace("Java","Python"))
## strip(): for removing the blank spaces
a="     Nazeer   Basha is the good  boy  super      guy          "
print(len(a))
b=(a.strip())
print(len(b))
## split():- will plit and gives a string
x="GOOD MORNING HYDERABAD"
y=x.split(" ")  # Based on spaces
print(y)
print(type(y))
emp="101,David,Manager,255000" ## Split based on comma
y=(emp.split(","))
print(y[0])
print(y[3])
print(y[2])
## format():- for substractions
x="{} is the capitan of indian cricket team"
print(x.format("Virat kohli"))
y="{} is the {} of {}"
print(y.format("Delhi","Capital","India"))

s="Iam nazeer and my age is {}"
age=25
print(s.format(age))

## sorted:
a="Happy Birth Day ra nazeer how are you man of the decade"
print(sorted(a))

## count():- to count the no of occurances of sub string of a character
x=" hello how are you hello man heloo hello"
print(x.count("hello"))
print(x.count("h"))

## find():- to check weather substring avilable or not, if avilable it returns first charactor of the
##          substring else it returs -1

x="python is easier than java"
print(x.find("java"))
print(x.find("Python"))

## String slicing: Extracting particular portion of a string
x="heloo Hyderabad"
print(x[2])
print(x[0:5])
print(x[0:9])
print(x[9:6]) ## gives a empty string caz slicing in forward direction
print(x[-9:-6]) ## -ve indexing
print(x[0])
print(x[:7])
print(x[5:])
print(x[:])
print(x[0:])
print(x[-9:9])
print(x[0:15:2])
print(x[0:15:3])
print(x[::-1])  # Reverse the string
print(x.index("H"))
print(x.find("H"))
## string functions:-
x="Happy Birthday Nazzu"
print(len(x))
print(max(x))
print(min(x))
print(x[:]+" Have a Great Day") ## String concatination
print("Hai "+x[15:])
print(x*3)
print(2*x)
## in or not in functions:
print("Nazzu" in x)
print("Nazzu" not in x)
print("day" in x)
print("u" in x)
print(x.count("a"))

print("---------------------------------------")



""" complex datatypes: A complex number is comprised of 2 parts
1.imaginary
2.real part
"""

x=3+5j
print(x)
print(type(x))
print(id(x))
print(x.real)
print(x.imag)
## we can also creat complex numbers by using complex() function:
x=complex(4,5)
print(x)
print(complex(5,10))
print(complex(10))
print(complex())
print(complex('4-4j'))   # Observe the string
print(complex(2.2,3.5))
print("---------------------------------------")

## OUTPUT Statements:--
x=10
y=20
z=30
print(x)
print(y)
print(x,y)
print(x,y,sep=" ")
print(x,y,sep=",")
print(x,y,sep="@")
print(x,y,sep="$")
print(x,y,sep="\t")  ## 4 spaces
print(x,y,sep=":")
print(x,y,sep="-->")
print(x,y,sep="\n")
print(x,y,sep=" ")
print(x,y,z,sep=" ")
print(x,y,z,sep=",")
print(x,y,z,sep=":")
print(x,y)
print(z,x)
print("x:y:z",x,y,z)
print("Cherry","Nazzu","Roja","Prasad",sep=",")
print("Cherry","Nazzu","Roja","Prasad",sep="@")
print('\n')  ## Two blank spaces bcz one for normal print and one for \n
print("good",end=" ")
print("Morning")

print("good",end=" ")
print("Morning",end=" ")
print("Nazzu")

print("good",end="\t")
print("Morning",end="\t")
print("Nazzu")

## output formating:
x=10;y=20
print("The vale of x {} and value {} ".format(x,y))
print("I Love Eating {} and Playing {}".format("Chicken","Cricket"))
print("I Love Eating {0} and Playing {1}".format("Chicken","Cricket"))
print("I Love Eating {} and Playing {}".format("Butter","Ludo"))
print("Hello {Name} Good {Greeting}".format(Greeting="Morning",Name="Nazzu"))
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))
x = 12.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %3.4f' %x)
print("-------------------------------")
"""
## INPUT Statements:-
fname=input("Enter First name:")
lname=input("Enter Last name:")
print("First Name:",fname)
print("Last Name:",lname)
print(fname+" "+lname)

# Accepting two values from use keyboard and performing addition

x=input("Enter x value: ")
y=input("Enter y value: ")
print(x)
print(type(x))    ## By default it will takes as strint so look the coad below
print(x+y)
print(x+" "+y)


x=int(input("Enter x value: "))
y=int(input("Enter y value: "))
print(x)
print(type(x))  
print(x+y)
"""

# Take the user information
Cname=input("Enter the coustemer Name:")
AcNo=int(input("Enter the A/c Details:"))
Balance=float(input("Balance:"))
Tamount=float(input("Balance to be transfered: "))

print("Customer Name:-" ,Cname)
print("Account Number:- ",AcNo)
print("Avilable Balance:- ",Balance)
print("Transferd Amount- ",Tamount)
print("Balance Left",Balance-Tamount)

p


