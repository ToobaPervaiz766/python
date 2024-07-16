Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#While loop 
count = 0
while(count<3):
    count = count+1
    print("Hello Greek")
 
 #single statement  While block

#count =0
#while(count== 0 ):print("Hello Greek")

#For in Loop
#Example 1
print("List Iteratoion")        
1 = ["Geeks","For","Geeks"]
for i in 1:
    print(i)


#Example 2
print ("Tuple Iteration")
t = ("Geeks","For","Geeks")
for i in t:
    print(i)

#Example 3

print("STRING Iteration") 
s = "Geeks"
for i in s:
    print(s)

#Iterating by index of Sequences

list = ["Geeks","for","Geeks"]

for index in range(len(list)):
    print (list[index])

#Loop Control Statements

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter: ',letter)
         var 10
#Break Statement
for letter in 'geeksforgeeks':
    if letter =='e' or letter == 's':
        break
    print("Current letter: ",letter)

#Creating  Funtions

def first_function():
    print("Hello from a function")
first_function()    

#Parameters
def first_function(fname):
    print(fname,"Whatever")
first_function("emil")  
first_function("gmil") 
first_function("fmil")   

#Default Parameter Value

def first_function(country = "Norway"):
    print("I am is From "+country)
first_function("sweden") 
first_function("India") 
first_function()   

#Passing a List as a Parameter

def first_function(food):
    for x in food:
        print(x)

fruit = ["apple","orange","bnana"]
first_function("fruit")        

#Returning values 

def first_function(x):
    return 5*x

... print(first_function(2) )  
... print(first_function(5) ) 
... print(first_function(10) ) 
... 
... #Keyword Arguments
... 
... def first_function(child3,child2,child1):
...     print("The youngest child is: "+child3)
... 
... first_function(child2 ="Tobias",child3="Emil",child1="Linus")
... 
... #create class
... 
... class myClass: x = 5
... 
... #Objects in Python
... 
... p1=myClass() 
... print(p1.x)
... 
... #The Init Function
... 
... class Person:
...    def _init_(self,name,age):
...       self.name=name
...       self.age = age
... p1=Person("John",36)
... 
... print(p1.name)
... print(p1.age)
... 
... #Object Methods
... 
... class Person:
...     def _init_(self,name,age):
...       self.name=name
...       self.age = age
... def myfun(self):
...     print("Hello My name is: "+self.name)
... 
...     p1 = Person("John",36)
