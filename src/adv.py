from room import Room
from player import Player
from item import Item


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

room['outside'].items.append(Item('knife', 'A sharp item to cut things'))
room['outside'].items.append(Item('light', 'which give a light in the room'))

room['foyer'].items.append(Item('pencil', 'Something to write with'))
room['foyer'].items.append(Item('paper', 'where you write'))

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

    if len(player.current_room.items) > 0:
        # print items in the room.
        print("The room container the following items:")
        for item in player.current_room.items:
            print(item)
    else:
        print("This room has no items for you to carry")        
# * Waits for user input and decides what to do.
    user_input = input("If you want to move to a different room please choose a direction ('N', 'S','E','W'):\n")
     # If the user enters "q", quit the game.
    if user_input.lower() == 'q':
        break
    split_input = user_input.split()
# If the user enters a cardinal direction, attempt to move to the room there.  
    if len(split_input)==1:
        if user_input.lower():
            attribute = split_input[0].lower()+"_to"
            if hasattr(player.current_room, attribute):
                player.current_room = getattr(player.current_room, attribute)        
            # Print an error message if the movement isn't allowed.    
            else:
                print(f"The {player.current_room.name} does not have {user_input} direction.")
                print(f"Please choose a different direction.")
                continue 
    elif len(split_input) == 2:        
        item_name = split_input[1]
        if split_input[0].lower() == 'get':
            item = player.current_room.get_item(item_name)
            if item:
                item.on_take()
                print(item)
                player.current_room.remove_item(item)
                player.items.append(item)
            else:
                print(f"{item_name} does not exist in the room.")
        elif split_input[0].lower() == "drop":
            # drop the item
            pass
        else:
            print("I did not recognize that command")        
            continue


