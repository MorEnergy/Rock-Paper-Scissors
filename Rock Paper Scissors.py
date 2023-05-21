import random
rock = '''
    ______
---'   ___)
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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

signs = [rock, paper, scissors]

if user_choice >=3 or user_choice <=-1:
  print("Pick a valid number!")
else:
  computer_choice = random.randint(0,2)
  picks = ["Rock", "Paper", "Scissors"]
  print(signs[user_choice])
  
  computer_select = picks[computer_choice]
  print(f"\nComputer chose: {computer_select}")
  print(signs[computer_choice])

  if user_choice > computer_choice:
    print("\nYou Win!")
  elif computer_choice > user_choice:
    print("\nYou Lose!")
  elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You Lose!")
  elif user_choice == computer_choice:
    print("\nDraw!")