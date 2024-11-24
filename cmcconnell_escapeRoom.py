def main():
    """ gets two choices, each choice determines the next action """
    
    getGame = {
        "start": ["You are trapped in a room. You need to get out, but then you see a door.", "Open the door", "door", "Search the room", "room"], 
        "door": ["You try and open the door, but it seems to be locked.", "Start over", "start", "Quit", "quit"], 
        "room": ["You look around the room and see", "A chest", "chest", "A shelf", "shelf"], 
        "chest": ["You open the chest and it explodes in your face.", "Start over", "start", "Quit", "quit"], 
        "shelf": ["It was just a regular shelf, what a waste of time.", "Check the rest of the room", "room", "Quit", "quit"], 
        "rug": ["You look at the rug, until you see a small bump. You lift up the rug and find a key. I wonder if this key will open the door. Only one way to find out.", "Go to the door", "go", "Keep searching the room", "keep"], 
        "closet": ["You look in the closet and fall into a deep hole. Now you are stuck.", "Start over", "start", "Quit", "quit"], 
        "go": ["Well what do you know, the key fits and the door opens. Suddenly you hear a noise behind you.", "Open the door", "open", "Check out the noise", "noise"], 
        "keep": ["You could have gotten out already. ", "Start over", "start", "Quit", "quit"], 
        "open": ["You have escaped the room. You win!", "Start over", "start", "Quit", "quit"], 
        "noise": ["You find out it was nothing, but the door slams shut and the key breaks. Now you are at square one.", "Start over", "start", "Quit", "quit"], 
    }
    
    playNode = "start"
    while True:
        description, *options = game[playNode]
        print(description)
        
        for i in range(1, len(options), 2):
            print(f"{i // 2 + 1}. {options[i]}")

        choice = input("What do you want to do? (Enter number or type 'quit' to exit) ")

        if choice.lower() == "quit":
            print("Thanks for playing!")
            break
        elif choice.isdigit() and 1 <= int(choice) <= (len(options) // 2):
            playNode = options[(int(choice) - 1) * 2 + 1]
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
   


