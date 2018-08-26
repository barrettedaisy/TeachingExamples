#text adventure seeq 2018
stuffList = ['flashlight','cleaning supplies','snack']

def main():
    print("you're cleaning a creepy old house when you hear a noise")
    print("you go into the next room to check it out")
    print("... all you have is your ", stuffList)
    room1()

def room1():
    print("welcome to room 1!")
    choice = raw_input("would you like to go to room (2) or room (3)?")
    if choice == "2":
        room2()
    elif choice == "3":
        room3()
    else:
        print("not a valid choice!")
        room1()

def room2():
    print("you're in room 2!")

def room3():
    print("now you're in room 3.....")



main() #start the game
    
