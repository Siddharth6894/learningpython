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

gesture = [rock,paper,scissors]
ges_val = len(gesture)

#User input code for the gesture
user_ges = int(input("Enter '0' for rock, '1' for paper and '2' for scissors: "))
if user_ges == 0: 
  print("You choose Rock:")
  print(gesture[0])
elif user_ges == 1:
  print("You choose Paper:")
  print(gesture[1])
elif user_ges == 2:
  print("You choose Scissor:")
  print(gesture[2])

#Computer code for the gesture
ran_ges = random.randint(0,ges_val-1)
if ran_ges == 0:
  print("Computer choose Rock")
  print(gesture[ran_ges])
elif ran_ges == 1:
  print("Computer choose Paper")
  print(gesture[1])
elif ran_ges == 2:
  print("Computer choose Scissors")
  print(gesture[2])

#Rock, Paper, Scissors logic

if user_ges == 0:
  if ran_ges == 1:
    print("Computer Won")
  elif ran_ges == 2:
    print("You Won")
  else:
    print("Its a tie")
elif user_ges == 1:
  if ran_ges == 0:
    print("You Won")
  elif ran_ges == 2:
    print("Computer Won")
  else:
    print("Its a tie")  
elif user_ges == 2:
  if ran_ges == 0:
    print("Computer Won")
  elif ran_ges == 1:
    print("You Won")
  else:
    print("Its a tie")
