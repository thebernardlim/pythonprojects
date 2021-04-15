import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
computerIndex = random.randint(0,2)

computerChoice = options[computerIndex]
playerIndex = int(input('Type 0 for Rock, 1 for Paper, 2 for Scissors'))

if (playerIndex < 0 or playerIndex >= 3):
  print("No such option!")
else:
  print("Player chose " + options[playerIndex])
  print("Computer chose " + options[computerIndex])
  if (playerIndex == computerIndex):
    print("Draw")
  elif(playerIndex == 0):
    if (computerIndex == 1): print("Computer Wins")
    elif (computerIndex == 2): print("Player Wins")
  elif(playerIndex == 1):
    if (computerIndex == 0): print("Player Wins")
    elif (computerIndex == 1): print("Computer Wins")
  elif(playerIndex == 2):
    if (computerIndex == 0): print("Computer Wins")
    elif (computerIndex == 1): print("Player Wins")
