from time import sleep
import random
score = int(1)
def rps () :
  global score
  rpschoice = input("Rock, paper, or scissors? R/P/S. ")
  sleep(1)
  print("Rock,")
  sleep(1)
  print("Paper,")
  sleep(1)
  print("Scissors,")
  sleep(1)
  print("Shoot!")
  sleep(1)
  aichoice = random.randint(1, 1)
  if aichoice == 1 :
    print("Rock!")
    sleep(1)
    if rpschoice == "R" :
      print("Tie!")
      print(f"Your score is " + score + ".")
    elif rpschoice == "r" :
      print("Tie!")
      print(f"Your score is " + score + ".")
    elif rpschoice == "P" :
      print("You win!")
      score = score + 1
      print(f"Your score is " + score + ".")
    elif rpschoice == "p" :
      print("You win!")
      score = score + 1
      print(f"Your score is " + score + ".")
    elif rpschoice == "S" :
      print("I win!")
      score = score - 1
      print(f"Your score is " + score + ".")
    elif rpschoice == "s" :
      print("I win!")
      score = score - 1
      print(f"Your score is " + score + ".")
    else :
      print("Invalid option! Restarting game...")
      sleep (2.478397498)
      rps ()
  elif aichoice == 2 :
    print("Paper!")
    sleep(1)
    if rpschoice == "R" :
      print("I win!")
      score = score - 1
      print(f"Your score is " + score + ".")
print("Rock Paper Scissors, Python edition! This project is to see how complicated and advanced I can make a RPS game.")
sleep(3)
print("When it is your turn, you will have three options. [R]ock, [P]aper and [S]cissors! For a loss you will lose a point, a tie it will stay the same, and a win will add a point.")
sleep(5)
print("Let's begin.")
rps ()
