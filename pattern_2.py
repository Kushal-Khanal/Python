def pattern(n):
  if(n==0):
    return  # This will halt program when n=0.
  print("*" * n)
  pattern(n-1)

n = int(input("Enter a positive number: "))
pattern(n)