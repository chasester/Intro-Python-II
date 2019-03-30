#utl functions - may move to new file


from utls import *
import operator

def getplayer():
    return player if(player) else debugprint("player has not been created but you tryed accessing it",True);

from room import Room
from player import Player
player = Player();
# Declare all the rooms
            
##room = {
##    'outside':  Room("Outside Cave Entrance",
##                     "North of you, the cave mount beckons"),
##
##    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
##passages run north and east."""),
##
##    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
##into the darkness. Ahead to the north, a light flickers in
##the distance, but there is no way across the chasm."""),
##
##    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
##to north. The smell of gold permeates the air."""),
##
##    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
##chamber! Sadly, it has already been completely emptied by
##earlier adventurers. The only exit is to the south."""),
##}


# Link rooms together

##room['outside'].n_to = room['foyer']
##room['foyer'].s_to = room['outside']
##room['foyer'].n_to = room['overlook']
##room['foyer'].e_to = room['narrow']
##room['overlook'].s_to = room['foyer']
##room['narrow'].w_to = room['foyer']
##room['narrow'].n_to = room['treasure']
##room['treasure'].s_to = room['narrow']
class _object:
    name = "";
    def __init__(self, name, direction=0):
        self.name = name;
        self.direction = direction;
    def on_look(self, lit):
        return True;
        
if __name__ == "__main__": #runs when called from this module
    print(getrelativedirection(0,5));
    while(True):
        r = Room("Outside");
        r.add_item(_object("hello"), r.monsters);
        r.on_look(30000);
        break;
    print(r.name);
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
