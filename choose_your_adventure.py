name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road. It has come to an end and you can go left or right. Which way would you like to go? (left/right) ").lower()

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across? (walk/swim) ").lower()
    if answer == "swim":
        print("You swam across and were eaten by a snake.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly. Do you want to cross it or head back? (cross/back) ").lower()
    if answer == "back":
        print("You went back the way you came and drove home.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no) ").lower()
        if answer == "no":
            print("The stranger became angry and stole your money.")
        elif answer == "yes":
            print("The stranger gave you a a magical map. You win!")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")