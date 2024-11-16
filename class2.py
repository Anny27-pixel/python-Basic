#number
x = 1        #int
y = 2.8 #float
z = 1j  #complex

x = 1
y = 36892896830960
z = -3255522

#int
print(type(x))
print(type(y))
print(type(z))

#float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


#float can be in the from of scientific number
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

#complex 
x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# type conversion
x = 1   #int
y = 2.8 #float
z = 1j  #complex

#convert from int to float
a = float(x)

#convert from float to int
b = int(y)

#convert from int to complex
c = complex(x)

print(a)
print(b)
print(c)

#random Number
import random

print(random.randrange(1,10))

#python casting
x = int(1) # x will be 1
z = float("3") #z will be 3.0
x = str("s1")  # x will be 's1'

#Assigning multiple string
a = """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Esse commodi, iste officiis voluptates aliquam nihil autem doloremque enim earum sunt aliquid cum cumque optio voluptatibus itaque a ab blanditiis beatae."""

print(a)

#String as an array
a = "Hello, World!"
print(a[1])

#Looping through string
for x in "banana":
    print(x)

#string length
a = "Hello, World!"
print(len(a))

#check the string either present
txt = "The best things in life are free!"
print("free" in txt)  # in keyword
if "free" in txt:
    print("yes, 'free is present")

print("expensive" not in txt)  # not in keyword
if "expensive" not in txt:
    print("No, 'expensive' is NOT present")

#slicing
b = " Hello, World!"
print(b[2:5])
print(b[2:])
print(b[-5:-2])
print(b[1:3])
print(a.upper())
print(a.lower())

#remove white space
a = " Hello,  World! "
print(a.strip())    #returns "Hello, world!"

a = "Hello, World!"
print(a.replace("H", "J"))
print(a.split(","))

age = 36
txt = "My name is John, I am " + str(age)
print(txt)

# f-string in python 3.6
txt = f"My name is John, I am  {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#math operation
txt = f"The price is {20*59} dollars"
print(txt)

#Boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9)

class myClass():
    def __len__(self):
        return 0
    
myObj = myClass()
print(bool(myObj))

def myFunction():
    return True

print(myFunction())

def myFunction():
    return True

if myFunction():
    print("YES!")

else:
    print("NO!")
