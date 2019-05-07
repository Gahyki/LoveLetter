from random import *
from deck import *
from Player import *
import time

#Setting up the cards in play then shuffle.
LoC = [1] * 6 + [2] * 4 + [3] * 4 + [4] * 4 + [5] * 3 + [6] * 2 + [7] + [8]
shuffle(LoC)
a = deck()

#One card must be removed to increase difficulty of the game. You do not know what card has been remove to lower the predictibility.
lastcard = LoC[0]

#Stacking up the cards
for element in LoC[1:]:
    a.push(element)

#Main Menu
def getinteger():
    '''The input makes sure it is an integer'''
    while True:
        answer = input("Enter the number of players who will play the game(3 to 6 players): ")
        try:
            A = int(answer)
            if A > 6:
                print("The number exceeds the MAXIMUM number of players. Try again.")
            elif A < 3:
                print("The number is lower than the MINIMUM number of players. Try again.")
            else:
                break
        except ValueError:
            print(answer, "That is not an option! Try again!")
    return A

def tester(lst):
    '''Takes a list to check if there is only one player that has not been eliminated.'''
    t = 0
    for x in lst:
        if x != "eliminated":
            t += 1
    if t > 1:
        return
    else:
        return 1

def compare(maxvalue, plyerlst):
    '''It takes a value and a list to run the program. It appends the player numbers of the biggest value and returns a list of winning players.'''
    playernumbers = []
    for i in range(len(plyerlst)):
        if plyerlst[i] == maxvalue:
            playernumbers.append(i + 1)
    return playernumbers

def LoveLetter():
    '''The full game.'''
    End = len(LoC[1:])                              #Counter to see when to end.
    P = [Player() for x in range(getinteger())]     #List of players
    pname = 1                   #Player names
    for x in P:                 #Hand out 1 card to each player first
        draw = a.draw()
        x.take(draw)
        print("Hello Player", str(pname) + ", your card first card is", str(x.card) + ".\n")
        time.sleep(1.5)
        End -= 1
        pname += 1
    while End != 0:
        pname = 1                       #Reset Player name number
        for element in P:               #Each player's turn
            #Abilities (Local functions)
            def ace(x):
                '''Guess another player's card. If you guess correctly, they are eliminated. You can guess your own card to do nothing.'''
                while True:
                    try:
                        select = int(input("Choose the player number whose card you would like to guess: ")) - 1
                        break
                    except ValueError:                                          #Error handling
                        print("That is not an option. Try again.")
                while not(0 <= select) or not(select < len(P)):                 #If player number is bigger or smaller than the number of players
                    select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                while P[select] == "eliminated":                                #If the chosen player is eliminated, choose again
                    select = int(input("This player has already been eliminated. Choose a different player: ")) - 1
                    while not(0 <= select) or not(select < len(P)):             #If player number is bigger or smaller than the number of players
                        select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                if pname == select + 1:                         #If you choose yourself, nothing happens
                    print("You used the card on yourself, so nothing happened.")
                    return
                else:
                    while P[select].ability:                    #Check if there is a shield
                        select = int(input("This player has a shield. Choose a different player number: ")) - 1
                        while not(0 <= select) or not(select < len(P)):             #If player number is bigger or smaller than the number of players
                            select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                        if pname == select + 1:                 #If you choose yourself, nothing happens
                            print("You used the card on yourself, so nothing happened.")
                            return
                    while True:
                        try:
                            guess = int(input("Enter a number from 1 to 8 to guess the card: "))
                            break
                        except ValueError:                                      #Error handling
                            print("That is not an option. Try again.")
                    if (P[select].card or P[select].newcard) == guess:
                        P[select] = "eliminated"
                        print("You are right! Player", str(select + 1) + ", you have been eliminated.")
                    else:
                        print("You did not guess the right card.")
                    
            def two(x):
                '''Look at another player's card. You can look at your own card to do nothing.'''
                while True:
                    try:
                        select = int(input("Choose the player number whose card you would like to see: ")) - 1
                        break
                    except ValueError:                                          #Error handling
                        print("That is not an option. Try again.")
                while not(0 <= select) or not(select < len(P)):                 #If player number is bigger or smaller than the number of players
                    select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                while P[select] == "eliminated":                                #If the chosen player is eliminated, choose again
                    select = int(input("This player has already been eliminated. Choose a different player: ")) - 1
                    while not(0 <= select) or not(select < len(P)):             #If player number is bigger or smaller than the number of players
                        select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                if pname == select + 1:                         #If you choose yourself, nothing happens
                    print("You used the card on yourself, so nothing happened.")
                    return
                while P[select].ability:                        #Check if there is a shield
                    select = int(input("This player has a shield. Choose a different player number: ")) - 1
                    while not(0 <= select) or not(select < len(P)):             #If player number is bigger or smaller than the number of players
                        select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                    if pname == select + 1:                     #If you choose yourself, nothing happens
                        print("You used the card on yourself, so nothing happened.")
                        return
                print("Player",str(select + 1), "has the card", str(P[select].card) + ".")

            def three(x):
                '''Duel with another player. You can duel yourself to do nothing.'''
                while True:
                    try:
                        select = int(input("Choose the player number whose card you would like to duel: ")) - 1
                        break
                    except ValueError:                                          #Error handling
                        print("That is not an option. Try again.")
                while not(0 <= select) or not(select < len(P)):                 #If player number is bigger or smaller than the number of players
                    select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                while P[select] == "eliminated":                                #If the chosen player is eliminated, choose again
                    select = int(input("This player has already been eliminated. Choose a different player: ")) - 1
                    while not(0 <= select) or not(select < len(P)):             #If player number is bigger or smaller than the number of players
                        select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                if pname == select + 1:                         #If you choose yourself, nothing happens
                    print("You used the card on yourself, so nothing happened.")
                    return
                while P[select].ability:                        #Check if there is a shield
                    select = int(input("This player has a shield. Choose a different player number: ")) - 1
                    while not(0 <= select) or not(select < len(P)):             #If player number is bigger or smaller than the number of players
                        select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                    if pname == select + 1:                     #If you choose yourself, nothing happens
                        print("You used the card on yourself, so nothing happened.")
                        return
                #If ability card is on the left hand, then the card on the right is compared
                if x == "L":
                    if P[select].card < P[pname - 1].newcard:
                        print("Your opponent had the card", str(P[select].card), "and your card was", str(P[pname - 1].newcard) + ".")
                        print("You have won the duel. Player", str(select + 1), "has been eliminated.")
                        P[select] = "eliminated"
                    elif P[select].card > P[pname - 1].newcard:
                        print("Your opponent had the card", str(P[select].card), "and your card was", str(P[pname - 1].newcard) + ".")
                        print("You have lost the duel, so you have been eliminated.")
                        P[pname - 1] = "eliminated"
                    else:
                        print("Both cards had the same value. It is a draw, so nothing happened.")
                #If ability card is on the right hand, then the card on the left is compared
                elif x == "R":
                    if P[select].card < P[pname - 1].card:
                        print("Your opponent had the card", str(P[select].card), "and your card was", str(P[pname - 1].card) + ".")
                        print("You have won the duel. Player", str(select + 1), "has been eliminated.")
                        P[select] = "eliminated"
                    elif P[select].card > P[pname - 1].card:
                        print("Your opponent had the card", str(P[select].card), "and your card was", str(P[pname - 1].card) + ".")
                        print("You have lost the duel, so you have been eliminated.")
                        P[pname - 1] = "eliminated"
                    else:
                        print("Both cards had the same value. It is a draw, so nothing happened.")
                    
            def four(x):
                '''You gain a shield'''
                element.ability = True
                print("You now have a shield.")

            def five(x):
                '''You make the person of your choice discard their card to draw another. If the person has an 8, they are dead. This includes yourself.'''
                while True:
                    try:
                        select = int(input("Choose the player number whose card you would like to burn: ")) - 1
                        break
                    except ValueError:                                          #Error handling
                        print("That is not an option. Try again.")
                while not(0 <= select) or not(select < len(P)):                 #If player number is bigger or smaller than the number of players
                    select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                while P[select] == "eliminated":                                #If the chosen player is eliminated, choose again
                    select = int(input("This player has already been eliminated. Choose a different player: ")) - 1
                    while not(0 <= select) or not(select < len(P)):             #If player number is bigger or smaller than the number of players
                        select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                while P[select].ability:                        #Check if there is a shield
                    select = int(input("This player has a shield. Choose a different player number: ")) - 1
                    while not(0 <= select) or not(select < len(P)):             #If player number is bigger or smaller than the number of players
                        select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                if P[select].card == 8:                                         #If the target has an 8
                    P[select] = "eliminated"
                    print("Player", str(select + 1), "has been eliminated.")
                    return
                getnew = a.draw()
                if select + 1 == pname:                                         #Draw a new card if you use on yourself
                    print("You discarded your hand and drew a new card.")
                    if x == "L":
                        P[select].newcard = getnew
                    elif x == "R":
                        P[select].card = getnew
                else:                                                           #If it's a different player
                    print("Player", str(select + 1), "had the card", str(P[select].card) + ".")
                    P[select].card = getnew
    
            def six(x):
                '''You can trade cards with a player of your choice. If you can trade with yourself to do nothing.'''
                while True:
                    try:
                        select = int(input("Choose the player number whose card you would like to exchange with: ")) - 1
                        break
                    except ValueError:                                          #Error handling
                        print("That is not an option. Try again.")
                while not(0 <= select) or not(select < len(P)):                 #If player number is bigger or smaller than the number of players
                    select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                while P[select] == "eliminated":                                #If the chosen player is eliminated, choose again
                    select = int(input("This player has already been eliminated. Choose a different player: ")) - 1
                    while not(0 <= select) or not(select < len(P)):             #If player number is bigger or smaller than the number of players
                        select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                if pname == select + 1:                         #If you choose yourself, nothing happens
                    print("You used the card on yourself, so nothing happened.")
                    return
                while P[select] == "eliminated":
                    print("Player", str(select + 1), "has already been eliminated.")
                    select = int(input("Choose a different player number: "))
                    while not(0 <= select) or not(select < len(P)):             #If player number is bigger or smaller than the number of players
                        select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                while P[select].ability:                        #Check if there is a shield
                    select = int(input("This player has a shield. Choose a different player number: ")) - 1
                    while not(0 <= select) or not(select < len(P)):             #If player number is bigger or smaller than the number of players
                        select = int(input("This player number does not exist. Pick a different player number: ")) - 1
                    if pname == select + 1:                     #If you choose yourself, nothing happens
                        print("You used the card on yourself, so nothing happened.")
                        return
                #Trading cards with the non 6 card
                if element.newcard == 6:
                    P[select].card, element.card = element.card, P[select].card
                elif element.card == 6:
                    P[select].card, element.newcard = element.newcard, P[select].card

            def seven(x):
                '''You must play this card if your other card is a 5, 6 or 8. It does nothing.'''
                return

            def eight(x):
                '''This card has no special ability.'''
                return

            if tester(P):
                pass
            elif element == "eliminated":                       #If the player is eliminated then skip
                pass
            else:
                element.ability = False                         #Remove the shield if there was one
                pick = a.draw()
                element.ncard(pick)
                print("Player", pname, "you have the cards", str(element.card), "and", str(element.newcard) + ".")
                if (element.card == 7 or element.newcard == 7) and (element.card == (5 or 6 or 8) or element.newcard == (5 or 6 or 8)):     #Conditions to play the card 7
                    print("Since you have the card 7 and the other card is either a 5 or 6 or 8, you had to play the card 7.")
                    if (element.card == 7) and (element.newcard == (5 or 6 or 8)):
                            element.card, element.newcard = element.newcard, None
                    elif (element.newcard == 7) and (element.card == (5 or 6 or 8)):
                            element.newcard = None
                    print("You now have the card", str(element.card) + ". \n")
                    time.sleep(1.5)
                else:
                    while True:
                        choose = input("Enter the card of your choice(L/R): ").capitalize()
                        #Dictionary for card values
                        powers = {1 : ace, 2 : two, 3 : three, 4 : four, 5 : five, 6 : six, 7 : seven, 8 : eight}
                        if choose == "L":
                            powers[element.card](choose)
                            if element.card == 5:               #When a five is played an extra card is removed from the deck than usual.
                                End -= 1
                            #If you die to the effect of your own card
                            if element == "eliminated":         #If you are eliminated, you don't have anymore cards in hand.
                                break
                            element.card, element.newcard = element.newcard, None
                            print("You now have the card", str(element.card) + ". \n")
                            break
                        elif choose == "R":
                            powers[element.newcard](choose)
                            if element.newcard == 5:            #When a five is played an extra card is removed from the deck than usual.
                                End -= 1
                            #If you die to the effect of your own card
                            if element == "eliminated":         #If you are eliminated, you don't have anymore cards in hand.
                                break
                            element.newcard = None
                            print("You now have the card", str(element.card) + ". \n")
                            break
                        else:
                            print("That is not an option. Please try again.")
                        time.sleep(1.5)
            End -= 1
            pname += 1
            if End == 0:                                        #When there are no cards left in deck, stop.
                break
    print("The game is over.")
    if not(tester(P)):
        print("Everyone, please show your hand.")
        pname = 1
        for x in P:
            if x != "eliminated":
                print("Player", str(pname), "has the card", str(x.card), "left.")
                pname += 1
            else:
                pname += 1
    time.sleep(0.5)
    print("The missing card was", str(lastcard) + ".")
    cval = []                                                   #List of card values
    for element in P:
        if element != "eliminated":
            cval.append(element.card)
        else:
            cval.append(0)
    wplayers = compare(max(cval), cval)                         #Finding the players with the highest card values
    time.sleep(1)
    if len(wplayers) == 1:
        print("The winner is Player", str(wplayers.pop()) + "!")#One winner
    else:
        w = []                                                  #List which the card values are strings
        for x in wplayers:
            w.append(str(x))
        win = " and ".join(w)                                   #String containing the winning players joined by "and"s
        print("The winners are Players", win + "!")             #Many winners

LoveLetter()
