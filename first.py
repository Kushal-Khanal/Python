# Code With Harry

print("Hello World!")

a = int(input("Enter number 1: "))

b = int(input("Enter number 2: "))

print("Number a is: ", a)
print("Number b is: ", b)
print("Sum is ", a + b)

#Lists
friends = ["Apple","Orange",5,345.06,False,"Askash","Rohan"] #Lists are like array

print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable.

print(friends[0])
print(friends[1:4]) #List slicing is same like string slicing. 
# Lists methods are: sort, reverse, append, insert, pop, remove.
a = () #tuples are immutable.

a = { "key" : "value",   #dictionary is mutable.
     "Kushal":"Mulpani",
     "marks":100,
     "list":[1,2,5]
     } 
a["key"] 

e=set() #empty set
s={1,5,32,54,5,5,5,"Kushal"} #set

for i in range(6):
  print(i)

for i in range(0, 100, 4):
     print(i)

# See different methods of lists, Tuple, Dictionary and Sets.   

# See chapter-9:(File IO)    