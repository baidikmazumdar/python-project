#Rock,Paper,Scissor game
import random
def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='R':
        if you=='S':
            return False
        elif you=='P':
            return True
    elif comp=='P':
        if you=='R': 
            return False
        elif you=='S':
            return True
    elif comp=='S':
        if you=='P':
            return False
        elif you=='R':
            return True           
print("Comp turn: Rock(R), Paper(P) or Scissor(S)")
randNo=random.randint(1,3)
# print(randNo)
if randNo==1:
    comp='R'
elif randNo==2:
    comp='P'
elif randNo==3:
    comp='S'
you=input("Player turn: Rock(R), Paper(P) or Scissor(S)")
a=gameWin(comp,you)
print(f'computer chose {comp}')
print(f'you chose {you}')
if a==None:
    print("The game is a tie")
elif a:
    print("you win")
else:
    print("you lose")


