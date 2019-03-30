#utl functions - may move to new file
#north is 0 and goes counter clockwise with 8 axis directions (n,nw,w,sw,s,se,e,ne)

from utls import *
import operator


from room import Room
# Declare all the rooms
            
room = {
    'outside':  Room.Create("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room.Create("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["bright", "beautiful", "well-lit"]),

    'overlook': Room.Create("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room.Create("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room.Create("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].to_n(room['foyer']);
room['overlook'].to_e(room['outside'], True);
room['narrow'].to_w(room['outside'], True);
room['foyer'].to_s(room['outside']);
room['foyer'].to_n(room['overlook']);
room['foyer'].to_e(room['narrow']);
room['overlook'].to_s(room['foyer']);
room['narrow'].to_w(room['foyer']);
room['narrow'].to_n(room['treasure']);
room['treasure'].to_s(room['narrow']);

class _object:
    name = "";
    def __init__(self, name, direction=0):
        self.name = name;
        self.direction = direction;
    def on_look(self, lit):
        return True;
        
if __name__ == "__main__": #runs when called from this module
    while(True):
        r = room["outside"];
        r.on_look(100);
        instr = input("");
        instr = instr.split(" ");
        if(instr[0] == "q" or instr[0]== "quit"): break;
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
