# Implement a class to hold room information. This should have name and
# description attributes.
import operator
import random;
import weakref;
from utls import *;
from describable import *;
from container import *;
from containable import *;
#from container import Container;
#from containable import Containable;


class Room(Describable, Container):
    monsters =[];
    traps=[];
    lit=0;
    attached_rooms = [None]*8;

    #name = name of the room to be used for indexing
    #items = items in this room
    #monsters = list of monsters this room contains
    #traps = list of traps this room contains
    #lit = light value to be passed in when looking in a room.
    #decription = describes the room
    #adjectives = adjectives to describe the room (order these in an order that would make sense if they were all useded, like [huge, decorated, breathe taking, magnificantly lit]
    #attch_rooms = the rooms that you can acess using cardidnal directions #added in cardient direction order stated in adv.py starting with N and moveing counter clockwise

    #below is a many variable way
    def Create(name, description="", adjectives=[], items=[], monsters=[], traps=[], lit=0, attached_rooms = []):
        return Room([name, description, adjectives, items, monsters, traps, lit, attached_rooms]);

    def __init__(self, arr):
        try:
            self.name = str(arr[0]);
            self.description = str(arr[1]);
            self.adjectives = arr[2];
            self.add_items(arr[3] if arr[3] is list else [arr[3]]);


            self.lit = int(arr[6]); #calc lit here
##            for i in range(0, len(arr[7])):
##                if(isinstance(arr[7][i], Room)):
##                    pass;
        except:
            debugprint("Not all arguments where given for room.");
        

        
    #for below funcitons item is any object owned by this class when parr is defined
   

    #def on_add_item(self, item): #use this for adding items to a map after load, say like dropping an item in the map;

    def on_look(self,lit): #when peaking lit will be lower but light source will be ignored # if player carries a light lit will be higher
        seen_items = [];
        seen_monsters = [];
        seen_traps = [];
        seen_rooms = [""]*8; #forces an list padded with 8 slots
        
        lit += self.lit;
        for i in self.items:
            if(_object(i).on_look(lit)): seen_items.append(i);

        for m in self.monsters:
            if(m.on_look(lit)): seen_monsters.append(m);

        for t in self.traps:
               if(t.on_look(lit)): seen_traps.append(t);
        for r in range(0, len(self.attached_rooms)):
            if self.attached_rooms[r] is None or not isinstance(self.attached_rooms[r],Room):
                continue;
            d = self.attached_rooms[r].on_look_doorway(r, lit);
            if(d in range(0, 8)): seen_rooms[d] = self.attached_rooms[r].getdescriptbydirection(lit,d);
        flag = False;
        flag = flag if flag else format_list_output(seen_items,"You see these Items:", operator.attrgetter('name'));
        flag = flag if flag else format_list_output(seen_monsters,"You see these Monsters:", operator.attrgetter('name'));
        flag = flag if flag else format_list_output(seen_traps,  "You see these Traps:", operator.attrgetter('name'));
        flag = flag if flag else format_direction_output(seen_rooms, "You see these Exits:");
        if not flag: print("You cant see anything.");
        

    def on_look_doorway(self,direction,lit):
        if(lit == -1): return -1; #rooms with a -1 lit are hidden rooms and will not be visible unless user examines
        lit += self.lit;
        player = getplayer();
        reldir = getrelativedirection(player.direction, direction);
        if(reldir == 0):
            return -1; #door im standing in
        if(reldir == 4): #straight across`
            return reldir if random.randint(min(100,lit*200),101) > 40 else -1;
        if(abs((reldir-4)) == 1): #is the door that is caticorner to the right or left
           return reldir if random.randint(min(100,lit*50), 101)> 40 else -1;
        return reldir if random.randint(min(100, lit*25),101) > 60 else -1; #all other entrances
        
    def on_item_take(self, item):
        if(item.tryremove()):
            return False;
        for i in traps:
            on_item_take(item);
        return true;
    
    def getdescriptbydirection(self, lit, d): #d is assumed relative direction
        lit += self.lit;
        output = "";
        print(lit);
        d = abs(d-4);
        for i in self.adjectives:
            output += ((i+" ") if(random.randint(min(100,lit*int((4-d)/4)),101) > 90) else '');
        output += ((" " + self.name) if(random.randint(min(100,lit*int((4-d)/4)),101) > 60) else " room");
        return output;

    def attach_room(self, direction, room, duel_attach=False):
        if(not isinstance(room, Room)): return debugprint("Trying to attach an object that is not of class Room");
        if(self == room): return debugprint("you cant attach a room to its self");
        if(direction >= len(self.attached_rooms)): return debugprint("Trying to attach a room out side the scope of direction");
        if(self.attached_rooms[direction] is not None): debugprint("Room is being forciable deattached");
        self.attached_rooms = insertdelete(self.attached_rooms, room, direction);
        if(duel_attach):
            room.attach_room(getoppisitedirection(direction),self, False); #False so that we dont get an endless loop :) thow this is an over define but this is here for a reminder

    def to_n(self, room, duel_attach=False):
        self.attach_room(0, room, duel_attach);
    def to_nw(self, room, duel_attach=False):
        self.attach_room(1, room, duel_attach);
    def to_w(self, room, duel_attach=False):
        self.attach_room(2, room, duel_attach);
    def to_sw(self, room, duel_attach=False):
        self.attach_room(3, room, duel_attach);
    def to_s(self, room, duel_attach=False):
        self.attach_room(4, room, duel_attach);
    def to_se(self, room, duel_attach=False):
        self.attach_room(5, room, duel_attach);
    def to_e(self, room, duel_attach=False):
        self.attach_room(6, room, duel_attach);
    def to_ne(self, room, duel_attach=False):
        self.attach_room(7, room, duel_attach);

if __name__ == "__main__":
    print("");#for unit testing
    import adv;
    b = Room(["outside"]);
    a = Room(["hello", "i exist", [], [], [], [], 100, [b]]);
    print(a.name);
    print(a.description);
    #a.on_look(100);
    #b.attach_room(0,a,False);
    #a.to_n(b, False);
    b.to_n(a, True);
    print(b.attached_rooms[0].name);
    print(a.attached_rooms[4].name);
