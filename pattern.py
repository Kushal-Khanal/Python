n = int(input("Enter the number: "))
for i in range(1, n+1):
  print(" " * (n-i), end="") # end="" is used to prevent python print() function to print a new line at the end.
  print("*" * (2*i-1), end="")
  print("")