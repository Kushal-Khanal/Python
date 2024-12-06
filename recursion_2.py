# Recursive function to calculate sum of first n natural numbers.
'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3

sum(n) = 1 + 2 + 3 + ... + n-1 + n
sum(n) = sum(n-1) + n
'''

def sum(n):
  if(n==1): #base condition to prevent negative values.
    return 1
  return sum(n-1) + n

n = int(input("Enter a positive number: "))
print(sum(n))