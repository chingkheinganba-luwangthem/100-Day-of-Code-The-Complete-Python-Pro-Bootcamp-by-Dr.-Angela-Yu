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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Diamond]
*******************************************************************************
''')
print('>>> Welcome to "Treasure Island Game"')
print('>>> Your mission is to find the treasure on Treasure Island.')

choice1 = input('>> To reach Treasure Island you have two options to travel. Type "boat" or "aeroplane" to choose your travel mode: ').lower()
if choice1 == "aeroplane":
    choice2 = input('>> You have arrived at "Captain Island" which is 500km away from the treasure. Two options available: type "continue" to continue by aeroplane or type "boat" to travel by boat to Treasure Island: ').lower()
    if choice2 == "continue":
        choice6 = input('>> You have arrived at Treasure Island. You are travelling through a forest and found three roads. Type "left", "straight", or "right" to continue: ').lower()
        if choice6 == "left" or choice6 == "right":
            castle = input('>> You have reached the final location. There are 4 rooms to choose from. Type "red", "green", "yellow", or "blue" to open the right room where the treasure is kept: ').lower()
            if castle == "red":
                print(">> You win! You found the treasure, great work!")
            else:
                print(">> You opened the room with fire. You lose. Game Over!")
        else:
            print(">> The road you chose leads to the sea and there is no further road to travel. Game Over!")
    else:
        print(">> The boat you chose crashed near Treasure Island. Game Over!")

elif choice1 == "boat":
    choice4 = input('>> You have reached "Chend Island" which is 800km away from Treasure Island. You need to change to an upgraded boat. There are 3 boats: type "red", "blue", or "green" to choose: ').lower()
    if choice4 == "green" or choice4 == "yellow":
        choice5 = input('>> You have arrived at Treasure Island. You are travelling through a forest and found three roads. Type "left", "straight", or "right" to continue: ').lower()
        if choice5 == "left" or choice5 == "right":
            castle = input('>> You have reached the final location. There are 4 rooms to choose from. Type "red", "green", "yellow", or "blue" to open the right room where the treasure is kept: ').lower()
            if castle == "red":
                print(">> You win! You found the treasure, great work!")
            else:
                print(">> You opened the room with fire. You lose. Game Over!")
        else:
            print(">> The road you chose leads to the sea and there is no further road to travel. Game Over!")
    else:
        print(">> The boat you chose ran out of fuel in the middle of the journey. Game Over!")
else:
    print(">> Invalid choice. Game Over!")
