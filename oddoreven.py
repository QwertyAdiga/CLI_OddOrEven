import random

choice = ["0","1","2","3","4","5","6"]#it is conidered as string 
ooe_choice = [0,1,2,3,4,5,6]#it is considered as int. so if we compare with int user input, this must be used
spl_choice = ["bat","ball"]

def oddoreven():
 while True:
   com_choice = random.choice(ooe_choice)
   odd_or_even = input("Choose odd or even :- ").lower()
   if odd_or_even == "odd":
      odd = int(input(f"Enter {choice} :- "))
      if odd in ooe_choice:
         if (odd + com_choice) % 2 == 0:
            odd_com = random.choice(spl_choice)
            if odd_com == "bat":
              print("Computer choose :-",com_choice,"\nYou choose :-",odd_or_even,"\nSum of your value is :- even","\nComputer choose :- batting","\nSo you are now doing :- balling\n")
              ball()
              break
            elif odd_com == "ball":
              print("Computer choose :- ",com_choice,"\nYou choose :-",odd_or_even,"\nSum of your value is :- even","\nComputer choose :- balling","\nSo now you are doing :- batting\n")
              bat()
              break 
         elif (odd + com_choice) % 2 != 0:
           print("Computer choose :-",com_choice,"\nYou choose :-",odd_or_even,"\nSum of your value is :- odd","\nNow you have got the opportunity to choose bat / ball\n")
           main()
           break
      else:
         print(f"Please enter {choice}")
   elif odd_or_even == "even":
      even = int(input(f"Enter {choice} :- "))
      if even in ooe_choice:
         if (even + com_choice) % 2 == 0:
            print("Computer choose :-",com_choice,"\nYou choose :-",odd_or_even,"\nSum of your value is :- even","\nNow you have got the opportunity to choose bat / ball\n")
            main()
            break
         elif (even + com_choice) % 2 != 0:
            even_com = random.choice(spl_choice)
            if even_com == "bat":
               print("Computer choose :- ",com_choice,"\nYou choose :-",odd_or_even,"\nSum of your value is :- odd","\nComputer choose :- batting","\nSo you are now doing :- balling\n")
               ball()
               break
            elif even_com == "ball":
               print("Computer choose :- ",com_choice,"\nYou choose :-",odd_or_even,"\nSum of your value is :- odd","\nComputer choose :- balling","\nSo now you are doing :- batting\n")
               bat()
               break
      else:
         print(f"Please enter {choice}")
   else:
      print("Please choose odd / even")
      continue

def main():
 while True:
    choose = input('''Enter "bat" / "ball" :- ''').lower()
    
    if choose == "bat":
        print("You choose batting\n")
        bat()
        break
    elif choose.lower() == "ball":
        print("You choose balling\n")
        ball()
        break
    else:
        print('''Please enter "bat" / "ball"\n''')
        continue

def bat():
 user_points = 0
 com_points = 0
 while True:
    com_choice = random.choice(choice)
    user_bat = input(f"Enter {choice} :- ")
    if user_bat in choice:
        if user_bat == com_choice:
            print("You choose :-",user_bat,"and your computer choose :- ",com_choice)
            print("Your points :-",user_points,"and your computer's points :- ",com_points,"\nSo you are now out and will do balling\n")
            break 
        else:
          user_points = user_points + int(user_bat) 
          print("You choose :-",user_bat,"and your computer choose :- ",com_choice)
          print("Your points :- ",user_points,"and your computer's points :- ",com_points)
          print("Continue the game\n")
          continue
    else:
        print(f"Please enter {choice}\n") 
 while True:
            com_choice = random.choice(choice)
            user_ball = input(f"Enter {choice} :- ")
            if user_ball in choice:
              if user_ball == com_choice:
                  print("You choose :-",user_ball,"and your computer choose :- ",com_choice)
                  print("Your points :-",user_points,"and your computer's points :- ",com_points)
                  if user_points > com_points:
                     print("Hurray!!. You won the match.")
                     break
                  elif user_points == com_points:
                     print("Oh!! it's a tie.")
                     break
                  else:
                     print("Oops!! your computer won the match.")
                     break
              else:
                  com_points = com_points + int(com_choice)
                  print("You choose :-",user_ball,"and your computer choose :- ",com_choice)
                  print("Your points :- ",user_points,"and your computer's points :- ",com_points)
                  if com_points > user_points:
                     print("Oops!! your computer won the match.")
                     break
                  else:
                     print("Continue the game\n")
                     continue                     
            else:
               print(f"Please enter {choice}\n")

def ball():
 user_points = 0
 com_points = 0
 while True:
    com_choice = random.choice(choice)
    user_ball = input(f"Enter {choice}:- ")
    if user_ball in choice:
       if user_ball == com_choice:
          print("You choose :-",user_ball,"and your computer choose :-",com_choice)
          print("Your points :-",user_points,"and your computer's points :-",com_points,"\nSo your computer is out and will do batting\n")
          break
       else:
          com_points = com_points + int(com_choice)
          print("You choose :-",user_ball,"and your computer choose :-",com_choice)
          print("Your points :-",user_points,"and your computer's points :-",com_points)
          print("Continue the game\n")
          continue       
    else:
       print(f"Please enter {choice}")
 while True:
    com_choice = random.choice(choice)
    user_bat = input(f"Enter {choice} :- ")
    if user_bat in choice:
       if user_bat == com_choice:
          print("You choose :-",user_bat,"and your computer choose :-",com_choice)
          print("Your points :-",user_points,"and your computer's points :-",com_points)
          if user_points > com_points:
             print("Hurray!!. You won the match.")
             break
          elif user_points == com_points:
             print("Oh!! it's a tie.")
             break
          else:
             print("Oops!! your computer won the match.")
             break
       else:
          user_points = user_points + int(user_bat)
          print("You choose :-",user_bat,"and your computer choose :-",com_choice)
          print("Your points :-",user_points,"and your computer's points :-",com_points)
          if user_points > com_points:
             print("Hurray!!. You won the match.")
             break
          else:
             print("Continue the game\n")
             continue
    else:
       print(f"Please enter {choice}")   
oddoreven()