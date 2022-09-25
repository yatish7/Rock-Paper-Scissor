#Rock Paper Scissor
print("*****Welcome to the Rock,Paper,Scissor game*****")
print("\nThis is a Multiplayer Game\n")
p1=input("Enter the name of Player 1? ")
p2=input("Enter the name of Player 2? ")
s1=s2=0
reply=input("Do you want to know the basic rules of the game(Yes/No)??")
if reply=='Yes':
  import Instructions
else:
    print("Alright then the game is about to start")
p=int(input("Enter how many points you want to play?"))
print("*****The game starts now*****")
while(1):
    if s1==p or s2==p:
        break
    else:
        p3=input(f"{p1} enter your choice(r/p/s)??")
        p4=input(f"{p2} enter your choice(r/p/s)??")
        if p3=='r' and p4=='p':
            print(f"{p2} wins this round")
            s2+=1
        elif p3=='p' and p4=='r':
            print(f"{p1} wins this round")
            s1+=1
        elif p3=='p' and p4=='s':
            print(f"{p2} wins this round")
            s2+=1
        elif p3=='s' and p4=='p':
            print(f"{p1} wins this round")
            s1+=1
        elif p3=='s' and p4=='r':
            print(f"{p2} wins this round")
            s2+=1
        elif p3=='r' and p4=='s':
            print(f"{p1} wins this round")
            s1+=1
        elif p3=='p' and p4=='p':
            print("Its a Draw..")
        elif p3=='r' and p4=='r':
            print("Its a Draw..")
        elif p3=='s' and p4=='s':
            print("Its a Draw..")
        else:
            print("Please enter valid input")
print("\n--------The game is Over--------\n")
print("*****Results Time*****\n")
if s1==p:
    print(f"{p1} has won the game")
    print(f"Score of {p1} is {s1}")
    print(f"Score of {p2} is {s2}")
else:
    print(f"\n{p2} has won the game\n")
    print(f"\nScore of {p1} is {s1}\n")
    print(f"\nScore of {p2} is {s2}\n")
print("\n*******Come back soon and play again*******\n")


    

                  
        
