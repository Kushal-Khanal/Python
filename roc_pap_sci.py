'''
-1 for Rock
0 for Paper
1 for Scissor
'''

import random

computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice(r || p || s): ")
youDict = {"r": -1, "p": 0, "s": 1}
reverseDict = {-1: "Rock", 0: "Paper", 1:"Scissor"}

you = youDict[youStr]

# By now we have two numbers (variables), you and computer.

print(f"You: {reverseDict[you]}\nComputer: {reverseDict[computer]}")

if(computer == you):
  print("DRAW!")

else:
  if(computer == -1 and you == 0):
    print("You Won!")

  elif(computer == -1 and you == 1):
    print("You Lose!")

  elif(computer == 0 and you == -1):
    print("You Lose!")

  elif(computer == 0 and you == 1):
    print("You Won!")   

  elif(computer == 1 and you == 0):
    print("You Lose!")

  elif(computer == 1 and you == -1):
    print("You Won!") 

  else:
    print("Something went wrong! Try again.")      