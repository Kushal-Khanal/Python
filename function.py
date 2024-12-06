#Function definition
def avg():
  a = int(input("Enter your number 1: "))
  b = int(input("Enter your number 2: "))
  c = int(input("Enter your number 3: "))

  average = (a + b + c)/3
  print(average)

avg()  #function call
print("This is your first average.")
avg()  
print("This is your second average.")

#function with arguments
def goodDay(name, ending="Hey"): #default parameter
  print("Good Day, " + name) # or, print(f"Good Day, {name}")
  print(ending)

goodDay("Kushal", "Thank you")  
goodDay("Khanal", "Thanks")  
goodDay("Alice", "Welcome")  