import random
# Snake, Water Or Gun Game
def gameWin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
            if you == 'w':
                return False
            elif you == 'g':
                return True
    elif comp == 'w':
            if you == 'g':
                return False
            elif you == 's':
                return True 
    elif comp == 'g':
            if you == 's':
                return False
            elif you == 'w':
                return True                     
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'    
elif randNo == 3:
    comp = 'g'

you = input("Your Turn : Snake(s), Water(w), Gun(g) ?")
a= gameWin(comp, you)

print(f"Computer Chose {comp}")
print(f"You Chose {you}")

if a == None:
    print("The game is a tie")
elif a:
     print("You Win!")
else:
     print("You Lose!")