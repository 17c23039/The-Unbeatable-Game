import random
import time
scoreriddle = 0
print("Okay, here's a couple riddles for you! Please use lowercase only.")
select = rand.randint(1,5)
if select = 3 :
  print("I am real, I am fake. Some people have me thougb I am not desirable, some people have the opposite of me, which spoils them. However I am not tangible. What am I?")
  print("a) Oxygen")
  time.sleep(1)
  print("b) Happiness")
  time.sleep(1)
  print("c) Bitcoin")
  time.sleep(1)
  print("d) Nothing.")
  time.sleep(1)
  answer = input("What is your answer? a/b/c/d ")
  if answer == "d" :
    print("Correct!")
    scoreriddle = scoreriddle + 1
  else :
    print("Incorrect!")
elif select = 2 :
  print("What type of cheese is made BACKWARDS?")
  print("a) Cheddar")
  time.sleep(1)
  print("b) Edam")
  time.sleep(1)
  print("c) Yorkshire")
  time.sleep(1)
  print("d) Parmesan")
  time.sleep(1)
  answer = input("What is your answer? a/b/c/d ")
  if answer = "b" :
    print("Correct!")
    scoreriddle = scoreriddle + 1
  else :
    print("Incorrect!")
elif select 3 :
  print("What word is always pronounced incorrectly?")
  print("No options for this!")
  time.sleep(1)
  answer = input.lower("Enter the word here:")
  if answer == "incorrectly" :
    print("Correct!")
    scoreriddle = scoreriddle + 1
  else : 
    print("Incorrect-ly ;)")