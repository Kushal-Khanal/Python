# Fahrenheit to Celsius

def f_to_c(f):
  return 5*(f-32)/9

f = int(input("Enter temperature in fahrenheit: "))
c = f_to_c(f)
print(f"{round(c, 2)} °C")