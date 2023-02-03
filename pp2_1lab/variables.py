a = 1  #int type
b = "chess" #str type
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(type(x))
print(type(y))
print(type(z))
k="car"
j='car'
print(k+j)#there is no difference between '' and ""
N='wood'
n='stone'
print(N + n)#variable names are case sensitive
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"#u can use this variables

#this variables illegal
#2myvar = "John"
#my-var = "John"
#my var = "John"

#multiple var
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)


x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()