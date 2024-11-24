import json

""" taEditor.py
    a complete text adeventure editor
    includes node editor
    save and load in JSON format
"""

def main():
    """ Main game loop that runs the text-based game. """
    game_data = getDefaultGame()
    playGame(game_data)

def playGame(game):
    """ Plays the game until the player decides to quit. """
    playNode = "start"
    while True:
        playNode = playNode(game, playNode)
        if playNode == "quit":
            print("Thanks for playing!")
            break

def playNode(game, current_node):
    """ Plays out the current node in the game. """
    description, *options = game[current_node]
    print(description)

    for i in range(1, len(options), 2):
        print(f"{i // 2 + 1}. {options[i]}")

    choice = input("What do you want to do? (Enter number or type 'quit' to exit) ")

    if choice.lower() == "quit":
        return "quit"
    elif choice.isdigit() and 1 <= int(choice) <= (len(options) // 2):
        return options[(int(choice) - 1) * 2 + 1]
    else:
        print("Invalid choice. Please try again.")
        return current_node # Stay in the same node if the input is invalid

def getDefaultGame():
    """ Creates and returns the default game structure. """
    {
        "start": ["You are trapped in a room. You need to get out, but then you see a door.", "Open the door", "door", "Search the room", "room"],
        "door": ["You try and open the door, but it seems to be locked.", "Start over", "start", "Quit", "quit"],
        "room": ["You look around the room and see", "A chest", "chest", "A shelf", "shelf"],
        "chest": ["You open the chest and it explodes in your face.", "Start over", "start", "Quit", "quit"],
        "shelf": ["It was just a regular shelf, what a waste of time.", "Check the rest of the room", "room", "Quit", "quit"],
        "rug": ["You look at the rug, until you see a small bump. You lift up the rug and find a key. I wonder if this key will open the door. Only one way to find out.", "Go to the door", "go", "Keep searching the room", "keep"],
        "closet": ["You look in the closet and fall into a deep hole. Now you are stuck.", "Start over", "start", "Quit", "quit"],
        "go": ["Well what do you know, the key fits and the door opens. Suddenly you hear a noise behind you.", "Open the door", "open", "Check out the noise", "noise"],
        "keep": ["You could have gotten out already.", "Start over", "start", "Quit", "quit"],
        "open": ["You have escaped the room. You win!", "Start over", "start", "Quit", "quit"],
        "noise": ["You find out it was nothing, but the door slams shut and the key breaks. Now you are at square one.", "Start over", "start", "Quit", "quit"],
    }

def editNode(game):
    """ Edits a node in the game structure. """
    node_name = input("Enter the name of the node you want to edit: ")
    if node_name in game:
        print("Current node data:", json.dumps(game[node_name], indent=2))
    else:
        game[node_name] = ["", "", "", "", ""]
        print(f"Created new node: {node_name}")

    editField(game[node_name])
    return game[node_name]

def editField(node):
    """ Edits the fields of a given node. """
    for i in range(0, len(node), 2):
        print(f"Current value of field '{node[i]}': {node[i + 1]}")
        new_value = input("Enter new value (or press enter to keep current): ")
        if new_value:
            node[i + 1] = new_value

def saveGame(game):
    """ Saves the current game state to a file. """
    outFile = open("game.dat", "w") as file:
    json.dump(game, file, indent=2)
    outFile.close()
    print("Game saved.")
    inFile = open("game.dat", "r")
    gameDat = json.load(inFile)
    print(gameDat)
    
    inFile.close()

def loadGame():
    """ Loads the game state from a file. """
    inFile = open("game.dat", "r")
    gameDat = json.load(inFile)
    print(gameDat)
        print("Game loaded.")
        return game_data
    else:
        print("No saved game found.")
        return getDefaultGame()

if __name__ == "__main__":
    game_data = loadGame()
    main()
