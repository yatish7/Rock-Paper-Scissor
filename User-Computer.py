#Rock Paper scissor game with Computer
import random
class valid_character(Exception):
    pass
reply=input("Do you want to know how this game works and rules(s/no): ")
if reply=='s':
    import Instructions
print("\n ******* The Game is about to Start****** \n")
user_score=computer_score=0
points=0
def game():
    global user_name,user_score,computer_score,points
    user_score=computer_score=0
    user_name=input("Enter your name: ")
    points=int(input("Enter how many points match do you want to play: "))
    print("\n******** THE GAME STARTS NOW *********\n")
    while(1):
        if user_score==points or computer_score==points:
            break
        try:
          user_choice=input("Enter 'r' for 'rock','s' for 'scissor','p' for 'paper': ")
          if user_choice not in 'rsp':
            raise valid_character("Enter a valid character")
        except valid_character as e:
              print(e)
              continue
        computer_choice=random.choice(['r','p','s'])
        print(f"The computer choice is {computer_choice}")
        if computer_choice==user_choice:
            print("\nIts a Draw,no one gained ponts in this round.\n")
            print(f"{user_name}_score: ",user_score)
            print("Computer_score: ",computer_score)
        elif (computer_choice=='r') and (user_choice=='p'):
            print(f"\n {user_name} won this round as paper beats rock.\n")
            user_score+=1
            print(f"{user_name}_score: ",user_score)
            print("Computer_score: ",computer_score)
        elif (computer_choice=='s') and (user_choice=='r'):
             print(f"\n {user_name} won this round as rock beats scissor.\n")
             user_score+=1
             print(f"{user_name}_score: ",user_score)
             print("Computer_score: ",computer_score)
        elif (computer_choice=='p') and (user_choice=='s'):
             print(f"\n {user_name} won this round as scissor beats paper.\n")
             user_score+=1
             print(f"{user_name}_score: ",user_score)
             print("Computer_score: ",computer_score)
        elif (computer_choice=='r') and (user_choice=='s'):
             print("\n Computer won this round as rock beats scissor.\n")
             computer_score+=1
             print(f"{user_name}_score: ",user_score)
             print("Computer_score: ",computer_score)
        elif (computer_choice=='p') and (user_choice=='r'):
             print("\n Computer won this round as paper beats rock.\n")
             computer_score+=1
             print(f"{user_name}_score: ",user_score)
             print("Computer_score: ",computer_score)
        else:
             print("\n Computer won this round as scissor beats paper.\n")
             computer_score+=1
             print(f"{user_name}_score: ",user_score)
             print("Computer_score: ",computer_score)
game()
print("\n-------------------- THE GAME IS OVER --------------------\n")
print("\n ****** Results ****** \n")
print(f"The Score of {user_name} is ",user_score)
print(f"The Score of computer is {computer_score}")
if user_score==points:
    print(f"{user_name} has won the game")
else:
    print("Computer has won the game")
print(f"\nThanks for making me play the game {user_name}, really had a great time...")
print("--------Looking forward to playing with you again soon--------")
            
        
        
            
