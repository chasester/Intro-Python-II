#contians all the item classes
from containable import *;
from discribable import *;
from container import *;
import utls;

class Item(Describable, Containable):
    def __init__(self, name, description):
        if(type(self) is Item): #stop from letting the user call this directly so you can never make a class that is purely Describable
            debugprint("This is a base class do not contruct here", True);
        self.name = name;
        self.decription = description;
        
