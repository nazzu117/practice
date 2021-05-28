
import re

x="Zerox center is The in Nearby in Landmark in Maduranagar,SR Nagar,Hyderabad,india-500038"
y=re.findall("i.s",x)
print(y)
print(y,type(y),id(y))

if y:
    print("YES,All THE WORLD IN THE WORLD")
else:
    print("SUPER WOMEN")


# \d [0-9] \d+ \d{} \d\d\d\d


z=""" 101,Smith,100000
    Blake,102,454500
    30000,103,Miler """
a=re.findall("\d{6}",z)
print(a)
a=re.findall("[a-z]?",z)
print(a)
