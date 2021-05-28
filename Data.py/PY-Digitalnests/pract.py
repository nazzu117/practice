""" From the function perspection
A parameter is a variable that listed in side the functrion defination and
 A parameter is valu passed at function called

we have 5 ways/to pass parameters/arguments
1.positiona arguments
2.default arguments
3.keyword arguments
4.Arbetary arguments
5.Arberety keyword arguments 

#positional argumemnts

def details(username,password):
     print("Username:",username)
     print("Password:",password)
     print("{} is the username and {} is the password".format(username,password))
     pass
details("Nazzu","Nazzu@117")
details(input("Enter the user name:"),input("Enter the password:"))

def names(fname,lname):
    print("First name is:",fname)
    print("Last name is:",lname)
    print("Iam {} {}".format(fname,lname))
names("Rama","Devi")
names(input("Enter the first name:"),input("Enter the secound:"))

def item(sweet):
    print("My favourit sweet is ",sweet)
    print("my favourite sweet is {}".format(sweet))
item("Gulab Jamun") 


def absv(value):
    if value>0:
        print(value)
    else:
        print(-value)
absv(int(input("Enter the value to check:")))

def details(state,country="India"):
    print(country,"My country")
    print(state,"Is amy state")
    print("{} is my country , im proud of my {}".format(country,country))
    print("{} is my state".format(state))
details("AP")
details("Austrila")
details("United States of America") 


def details(username,password,designation="Developer",company="TCS",department="Softwear developement"):
     print("Username:",username)
     print("Password:",password)
     print("Designation:",designation)
     print("Company:",company)
     print("Department:",department)
     print("{} is the username and {} is the password working as {} at {} in {} departyment".format(username,password,designation,company,department))
     pass
details("Nazzu","Nazzu@117")
details(input("Enter the user name:"),input("Enter the password:"))

def greet(wish="Good Morning"):
    print("nazzu"+" "+wish)

greet()

def greets(name,wish="*****Eid mubarak*****"):
    print("Hello"+" "+name+","+wish)
greets("Nazzu")
greets("ElionMask","How do you do man..?")


def details(username,password,country="India",state="Telangan",city="Hyderabad"):
            print("Username:",username)
            print("Password:",password)
            print("Country:",country)
            print("State:",state)
            print("City:",city)
            print("{} is user name {} is the password and he is from {},{},{} ".format(username,password,country,state,city))
details(username="Nazeer",password=123456789)
details(password=123456789,city="Secundrabad",username="Midhun")
            
def family(child1,child2,child3):
    print(child1)
    print(child2)
    print(child3)
family(child1="Ussain",child2="Nazzu",child3="Haseena")

def family(*childrens):
    print(childrens)
    for i in childrens:
        print(i)
family("somesh","ramesh","suresh","naresh","mahesh")


def names(*people):
    for i in people:
      print("Hello ",people)
names("Ramesh","suresh","Mahesh","Naresh")

def trans(*a,name="Ramadevi"):
    b=sum(a)
    print(sum(a))
    print('{} is debited from {} account.'.format(b,name) )
trans(123.4,5655.9,5678.9,5454.4)
trans(6576.5,5565,554,900,444.2,6645)


def bank(*trans,accounts="Savings"):
    print("hi")
    print(sum(trans))
    print("{} is debited from {} account".format(sum(trans),accounts))
    print(accounts)

bank(123,123,444,555,33,190)

def myFun(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3) 
args = ("Geeks", "for", "Geeks") 
myFun(*args) 
  
kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
myFun(**kwargs) 


def abs_value(num):
    if num>=0:
        return num
    else:
        return -num
print(abs_value(int(input("Enter value to check abs value:"))))
print(abs_value(-9))
print(abs_value(9))
print(abs_value(-56))  

def get_even(numbers):
   return [num for num in numbers if not num % 2]
print(get_even([1, 2, 3, 4, 5, 6]))

def print_greeting():
    print("Hell Good Evening")
print(print_greeting())

def return_greeting():
    return "Hii Happy BirthDay"
print(return_greeting()) 

def add(a, b):
    result = a + b
    return result
add(2, 2)   

def factor(n):
    if n==0:
        return 1
    else:
        return n*(n-1)
result=factor((int(input("Enter the number:"))))
print(result)  

def reverse(x):
    return x[::-1]
mytext=reverse("The is the information that you have to reverse...@@@")
print(mytext)

def reversed(string):
    if len(string)==0:
        return string
    else:
        return (reverse(string[1:]+string[0]))
a = str(input("Enter the string to be reversed: "))
print(reverse(a))

def reverse(string):
    if len(string)==0:
        return string
    else:
        return string[::-1]
n=input("enter string: ")
print(reverse(n))

x = 12.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %3.4f' %x)  

#'p' + 'q' if '12'.isdigit() else 'r' + 's'

n=7
c=0
while(n):
    if(n>5):
        c=c+n-1
        n=n-1
    else:
        break
print(n)
print(c)

str1="hello"
c=0
for x in str1:
   if(x!="l"):
       c=c+1
   else:
       pass
print(c)
5

for j in [0,1,2,3,4]:
    print(j)


str1="learn python"

str2=""

str3=""

for x in str1:

    if(x=="r" or x=="n" or x=="p"):

        str2+=x

        pass

    if(x=="r" or x=="e" or x=="a"):

        str3+=x

print(str2,end=" ")

print(str3)"""



for i in range(0,2,-1):
    print("Hello")

x="55"
y=str(9)
print(x+y)


