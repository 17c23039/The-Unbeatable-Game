from random import randint
from time import sleep
print("Welcome to coin flip! Here, it is harder to win. You must win 3 times in a row to win!")
cfscore = 0
while cfscore < 3 :
  cfchoice = input("Heads or Tails? H/T. ")
  print(f"Okay, you picked {cfchoice}. I'll take the other option. Let's see the outcome.")
  cfoutcome = randint(1, 2)
  sleep(1)
  print("Spinning...")
  sleep(3)
  if cfoutcome == 1 :
    print("It's heads!")
    sleep(2)
    if cfchoice == "H" :
      print("You win!")
      cfscore = cfscore + 1
      print(f"Your score is {cfscore}!")
    elif cfchoice == "h" :
      print("You win!")
      cfscore = cfscore + 1
    elif cfchoice == "T" :
      print("You lose.")
      score = 0
      print("Your score is now " + score + ".")
    elif cfchoice == "t" :
      print("You lose.")
      score = 0
      print("Your score is now " + score + ".")
    else :
      print("Your option was invalid. Your score will not change.")
  elif cfoutcome == 2 :
    print("It's tails!")
    sleep (2)
    if cfchoice == "T" :
      print("You win!")
      cfscore = cfscore + 1
      print(f"Your score is {cfscore}!")
    elif cfchoice == "t" :
      print("You win!")
      cfscore = cfscore + 1
      print(f"Your score is {cfscore}!")
    elif cfchoice == "H" :
      print("You lose.")
      score = 0
      print("Your score is now " + score + ".")
    elif cfchoice == "h" :
      print("You lose.")
      score = 0
      print("Your score is now " + score + ".")
    else :
      print("Your option was invalid. Your score will not change.")
  sleep (2)
print("Well played. You've bested me. Twice.")
sleep(5)
print("Well, as you guessed, we aren't finished yet. Let's move onto game 3. ")
import tt