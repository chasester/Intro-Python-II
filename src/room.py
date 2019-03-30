# Implement a class to hold room information. This should have name and
# description attributes.
import operator
import random;
from utls import *;

class Room:
    name = "";
    items = [];
    monsters =[];
    traps=[];
    lit=0;
    attch_rooms = []

    #name = name of the room to be used for indexing
    #items = items in this room
    #monsters = list of monsters this room contains
    #traps = list of traps this room contains
    #lit = light value to be passed in when looking in a room.
    #decription = describes the room
    #adjectives = adjectives to describe the room (order these in an order that would make sense if they were all useded, like [huge, decorated, breathe taking, magnificantly lit]
    #attch_rooms = the rooms that you can acess using cardidnal directions
    
    def __init__(self, name, items=[], monsters=[], traps=[], lit=0, description="", adjectives=[], attch_rooms = []):
        self.name = str(name);
        if(items): self.add_items(items, self.items);
        if(monsters): self.add_items(monsters, self.monsters);
        if(traps): self.add_items(traps, self.traps);
        self.lit = lit;
        self.decription = description;
        self.adjectives = adjectives;
        self.attch_rooms = attch_rooms; #added in cardient direction order stated in adv.py starting with N and moveing counter clockwise

    #for below funcitons item is any object owned by this class when parr is defined
    def add_item(self,item, parr):
        parr.append(item);
        #item.on_add(self);

    def add_items(self,arr,parr):
        for i in arr:
            self.add_item(i,parr);

    def remove_item(self, item, parr):
        self.items.remove(item);
        item.on_remove();

    def remove_items(self, arr, parr):
        self.removeitem([i for i in arr], parr);
    
    def use_item(self, item, parr):
        if(item.on_use()):
            removeitem(item);

    #def on_add_item(self, item): #use this for adding items to a map after load, say like dropping an item in the map;

    def on_look(self,lit): #when peaking lit will be lower but light source will be ignored # if player carries a light lit will be higher
        seen_items = [];
        seen_monsters = [];
        seen_traps = [];
        seen_rooms = [None]*8; #forces an list padded with 8 slots

        lit += self.lit;
        print(len(self.items));
        print(len(self.monsters));
        print(len(self.traps));
        for i in self.items:
            if(_object(i).on_look(lit)): seen_items.append(i);

        for m in self.monsters:
            if(m.on_look(lit)): seen_monsters.append(m);

        for t in self.traps:
               if(t.on_look(lit)): seen_traps.append(t);
        for r in self.attch_rooms:
            d = r.on_look_doorway(self, lit);
            if(d in range(0, 9)): seen_rooms[d] = r.getdescriptbydirection(lit,d);
            
        if(len(seen_items)>0): format_list_output("You see these Items:", seen_items, operator.attrgetter('name'));
        if(len(seen_monsters)>0): format_list_output("You see these Monsters:", seen_monsters, 'name');
        if(len(seen_traps)>0): format_list_output("You see these Traps:", seen_traps, operator.attrgetter('name'));
        if(len(seen_rooms)>0): format_direction_output("You see:", seen_rooms);
        

    def on_look_doorway(self,direction,lit):
        if(lit == -1): return -1; #rooms with a -1 lit will are hidden rooms and will not be visible unless user examines
        lit += self.lit;
        player = getplayer();
        reldir = getrelativedirection(player.dir, direction, "across");
        if(reldir == 0):
            return -1; #door im standing in
        if(reldir == 4): #straight across
            return reldir if random.randint(min(100,lit*200),101) > 40 else -1;
        if(abs((reldir-4)) == 1): #is the door that is caticorner to the right or left
           return reldir if random.ranint(min(100,lit*50), 101)> 40 else -1;
        return reldir if random.ranint(min(100, lit*25),101) > 60 else -1; #all other entrances
        
    def on_item_take(self, item):
        if(item.tryremove()):
            return false;
        for i in traps:
            on_item_take(item);
        return true;
    
    def getdescriptbydirection(self, lit, d): #d is assumed relative direction
        lit += self.lit;
        output = "";
        d = abs(d-4);
        for i in self.adjectives:
            output += ((i+" ") if(random.randint(min(100,lit*int((4-d)/4)),101) > 40) else '');
        output += ((" " + self.name) if(random.randint(min(100,lit*int((4-d)/4)),101) > 40) else " room");


if __name__ == "__main__":
    print("");#for unit testing
    import adv;
