import random
c = ['r', 's', 'p']
games=int(input("Enter number of games: "))
wins=0
losses=0
draws=0
while True:
    n=str(input("Enter choice ([r]ock, [p]aper, [s]cissor, [q]uit: "))
    rand = random.choice(c)
    if (n=='r' and rand=='s') or (n=='s' and rand=='p') or (n=='p' and rand=='r'):
        wins= wins + 1
    elif (n=='r' and rand=='r') or (n=='s' and rand=='s') or (n=='p' and rand=='p'):
        draws=draws+1
    elif (n=='r' and rand=='p') or (n=='s' and rand=='r') or (n=='p' and rand=='s'):
        losses=losses+1
    elif n=='q':
        break
    else:
        print("Use valid command!!")
    total=wins+losses+draws
    print("Computer: ", rand)
    print("Wins-",wins,":","Loss-",losses,":","Ties-",draws,"total games-",total)
    if total==games:
        break
