class Employee:
  language = "Python" #This is a class attribute
  salary = 1200000

  def __init__(self) -> None: # Dunder method which is automatically called
    print("I am creating an object.")

  def getInfo(self):
    print(f"The language is {self.language}. The salary is {self.salary}")

  @staticmethod
  def greet():
    print("Good Morning")

kushal = Employee()
kushal.name = "Kushal" #This is a object or instance attribute
print(kushal.name, kushal.salary)   

rohan = Employee() #rohan is object