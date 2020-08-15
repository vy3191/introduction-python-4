from room import Room
from player import Player
# from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']



#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['foyer'])
# Write a loop that:
#
while True:
# * Prints the current room name
    print(f"Welcome to the Adventrue game.")
    print(f" You are current location is at {player.current_room.name} room.")
# * Prints the current description (the textwrap module might be useful here).
    print(f"and it looks like: {player.current_room.description}")
# * Waits for user input and decides what to do.
    user_input = input("If you want to move to a different room please choose a direction ('N', 'S','E','W'):\n")
# If the user enters a cardinal direction, attempt to move to the room there.
    if user_input.lower() == 'q':
        break
    if user_input.lower():
        attribute = user_input.lower()+"_to"
        if hasattr(player.current_room, attribute):
            player.current_room = getattr(player.current_room, attribute)
        else:
            print(f"The {player.current_room.name} does not have {user_input} direction.")
            print(f"Please choose a different direction.")
            continue

            


# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
