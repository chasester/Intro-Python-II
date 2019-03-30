debug = True;
forceStop = True if debug else False; #this can only be valid if the debug mode is active

cardinal_directions = { 'n': 0, 'nw': 1, 'w': 2, 'sw': 3, 's': 4, 'se': 5, 'e': 6, 'ne': 7 };

relative_directions = [ "behind", "near right", "right", "far right", "in front", "far left", "left", "near left" ]


#from player import Player
class Player:
    direction = 4;
player1 = Player();
def getplayer():
    return player1 if(player1) else debugprint("player has not been created but you tryed accessing it",True);

def debugprint(str, stop=False):
    if(debug):
        print(str);
    if(forceStop and stop):
        raise;

#if array is sorted,
def format_list_output(arr, prefix="", arrkey=None):
    try:
        if(not len(arr)):
            return False;
        if(prefix is not ""): print(prefix);
        if(True):
            arr.sort(key=operator.attrgetter(name));
        quanity = 1;
        for i in range(0, len(arr)):
            if(i < len(arr) and arr[i].name == arr[i].name):
                quanity += 1;
                continue;
            if(quanity < 1):
                debugprint(f"\tFound Item {arr[i].name} with no quanity.");
                continue;
            print(f"{'A' if quanity < 2 else str(quanity)} {arr[i].name}");
            quanity = 1;
        return True;
    except:
        debugprint("Must use array with items that contain a name property", True);
        return False;
    
def format_direction_output(arr,prefix=""): #keep in mind array must be stored based on relative direction to the player
    output = "";
    flag = False;
    try:
        if(prefix is not ""): output += prefix;
        for r in range(0,len(arr)):
            if(arr[r] is ""): continue;
            output += f"\n\t{toNameCase(relative_directions[r])}: {toNameCase(str(arr[r]))}";
            flag = True;
        if(flag): print(output);
        return flag;
    except:
        debugprint("Array must contian string convertable items",True);
        return False;

def getrelativedirection(d,d1):
    d = d1-d;
    if(d < 0): d = 8+d;
    return d; #if 0 in same corner, if 2 to the left, 6 to the right, if 4 stright accross. etc 

def getoppisitedirection(d):
   return (d+4)%8;

def insertdelete(arr,item, pos): #fix for weird referencing error when assigning an array element of an object to and object of the same type
    a = arr[:pos];
    a.append(item);
    ++pos;
    a.extend(arr[pos:]);
    return a;

def toNameCase(s):
	return " ".join([i.capitalize() for i in str(s).split(" ")]);

