print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ _______________|_________
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print('Welcome to the "Journey Through the Jungle" treasure quest!\nLet your intuition lead the way as you make choices to uncover hidden treasures,\nincluding exclusive community rewards, surprise gifts, and special event access.\nYour adventure starts now! \n')

choicea = input("You are standing at the edge of a dense jungle.\nTwo paths stretch out in front of you: one leads to a narrow trail cutting through the jungle,\nwhile the other follows a winding river. Where do you want to go? Left (narrow trail) or Right (riverbank)?\n").lower()

if choicea == "left":
    print("""Something about the mysterious narrow trail beckons you, so you decide to head left.
As you venture deeper into the jungle, the trees grow thicker, their twisted branches closing in like grasping fingers.
Shadows play tricks on your eyes as the sun\'s rays struggle to penetrate the dense foliage. Suddenly, you hear rustling 
in the nearby bushes. Your pulse quickens. Is it an animal? A hidden threat? Or maybe… something more?

Curiosity grips you, and despite your instincts to run, you decide to investigate. Slowly, you approach the bushes, 
pushing aside the leaves. To your amazement, a hidden cave entrance, almost entirely obscured by vines and moss, comes 
into view. The entrance is sealed by an ancient stone door covered in carvings—symbols you can\'t quite decipher. It radiates 
an air of mystery and power, as if it\'s been locked for centuries, keeping something either hidden or protected inside.

You search for a way to open the cave, but without a key or a map to guide you, it\'s impossible to unlock. Reluctantly, 
you realize you\'re not prepared to uncover its secrets—at least, not yet. With no other choice, you turn back to the 
jungle and make your way to the river path. \n""")
    choice1 = input('Please type "River" to continue exploring your journey.\n').lower()
    if choice1 == "river":
        choicea = "right"
if choicea == "right":
    print("""Something about the shimmering water and the sound of the gentle current draws you in. You decide
to go right, following the river\'s edge. The peaceful riverbank glistens under the sun, while the dense jungle across
beckons with mystery. Will you row across the calm waters to explore the far jungle, or follow the river downstream,
risking the unknown dangers ahead?\n""")
    choice2 = input('Type "Row" to row across the river, or "Stay" to stay and follow the river downstream.\n').lower()
    if choice2 == "stay":
        print("Walking downstream, you encounter a massive waterfall and are swept over the edge, ending in disaster. Game Over.")
    elif choice2 == "row":
        print("You row across the calm waters, reaching the far shore where two paths await your next choice.\n")
        choiceb = input('Where would you want to go? To the "Mountain", or to the "Dense Forest"?\n').lower()
        if choiceb == "dense forest":
            print("You wander aimlessly and get lost in the forest. Game Over.")
        elif choiceb == "mountain":
            print("You climb the mountain, leading to the next challenge.\n")
            choice3 = input('"Take the Map", or "Explore Further"?\n').lower()
            if choice3 == "explore further":
                print("You venture too far and fall off a cliff. Game Over.")
            elif choice3 == "take the map":
                choice4 = input('Take the map: You find the map! Type "Cave" to head to the cave for the next part of your adventure.\n').lower()
                if choice4 == "cave":
                    print("""As you step into the dark echoing cave, the air grows thick with mystery, and at the end of the
twisting labyrinth, two ancient boxes await — one promising riches, the other hidden danger.\n""")
                    choicec = input('Which one would you choose? The "Golden Box 1", or the "Golden Box 2"?\n').lower()
                    if choicec == "golden box 1":
                        print("The golden box 1 is a trap, sealing your fate. Game Over.")
                    elif choicec == "golden box 2":
                        print("You uncover the hidden treasure and win! Congratulations!")
                    else:
                        print("Oops! That\'s not a valid choice. Try again and stay on the right path! Game over.")
                else:
                    print("Oops! That\'s not a valid choice. Try again and stay on the right path! Game over.")
            else:
                print("Oops! That\'s not a valid choice. Try again and stay on the right path! Game over.")
        else:
            print("Oops! That\'s not a valid choice. Try again and stay on the right path! Game over.")
    else:
        print("Oops! That\'s not a valid choice. Try again and stay on the right path! Game over.")
else:
    print("Oops! That\'s not a valid choice. Try again and stay on the right path! Game over.")
