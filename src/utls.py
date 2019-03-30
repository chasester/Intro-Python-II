debug = False;
forceStop = True if debug else False; #this can only be valid if the debug mode is active

cardinal_directions = { 'n': 0, 'nw': 1, 'w': 2, 'sw': 3, 's': 4, 'se': 5, 'e': 6, 'ne': 7 };

relative_directions = { "behind", "near right", "right", "far right", "infront", "far left", "left", "near left" }


def debugprint(str, stop=False):
    if(debug):
        print(str);
    if(forceStop and stop):
        raise;

#if array is sorted,
def format_list_output(arr, prefix="", arrkey=None):
    try:
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
    except:
        debugprint("Must use array with items that contain a name property", True);

def format_direction_output(arr,prefix=""): #keep in mind array must be stored based on relative direction to the player
    try:
        if(prefix is not ""): print(prefix);
        for r in range(0,len(arr)):
            if(not arr[r]): continue;
            print(f"\t{relative_directions[r]}: {str(r)}.");
    except:
        debugprint("Array must contian string convertable items",True);

def getrelativedirection(d,d1):
    d = d1-d;
    if(d < 0): d = 8+d;
    return d; #if 0 in same corner, if 2 to the left, 6 to the right, if 4 stright accross. etc 
