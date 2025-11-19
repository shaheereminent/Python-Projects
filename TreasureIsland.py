print(r'''
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
/______/______/______/______/______/______/______/______/______/______[TomekK] 
*******************************************************************************
''')
print("Welcome to the treasure Island.\nYour mission is to find the treasure.")
print("Your missin is to find the treasure.")
cross_road = input("You are at cross road. Where do you want to go? Left or Right: ")

if cross_road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    wait_or_swim = input("""Type "wait" to wait for a boat. Type "swim" to swim across:  """)
    
    if wait_or_swim == "wait":
        print("You've arrived at the island unharmed. There is a house with 3 doors.")
        house_with_doors = input("One Red, One Yellow & One Blue. Which color do you choose? ")
        
        if house_with_doors == "yellow":
            print("You Won!")
        elif house_with_doors == "red":
            print("Burned by fire. Game Over!")
        elif house_with_doors == "blue":
            print("Eaten by beasts. Game Over!")
        else:
            print("Game Over.")
        
    else:
        print("Attacked by trout. Game Over!")
elif cross_road == "right":
    print("Game Over")
