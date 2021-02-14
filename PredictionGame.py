print("Welcome to my first game")
name = input("What is your name?")
age = int(input("What is your age?"))
health = 15
print("Hello",name, "! you are",age,"years old")

if(age>=18):
  print("you are old enough to play this game...")

  wants_to_play = input("Do you want to play the game?")
  answer = wants_to_play.lower()
  if(answer == 'yes'):
    print('lets play')
    print("You are starting with",health,"health")

    left_right = input('Select choice... Left or Right (Left/Right)?').lower()
    if(left_right == 'left'):
      ans = input("Nice, You follow the path and reach a lake... Do you swim across or go around (across/around)?").lower()
      if(ans == 'across'):
        health -= 5
        print(f"you managed to get across, but were bit by a fish and lost 5 health. Remaining health {health}")
        
      elif(ans == 'around'):
        print("You went around and reached the other side of the lake..")

      ans2 = input("You notice a house and a boat. which way do you go to?(house/boat)? ").lower()
      if(ans2 == "house"):
        print("You entered the house and hit by the furniture. You lost 10 health here..")
        health -= 10
        if(health <=0):
          print("You have 0 health. You Lost... Try Luck next time...")
        else:
          print(f"You have survived... You have {health}... You won... Congratulations!!!")
      else:
        print("you fell in the lake.. You lost.. Try luck next time..")    
      
        
    else:
      print("You fell down and lost... Play Again!!!")



  else:
    print('GoodBye...')
else:
  print("You are not enough to play this game...")