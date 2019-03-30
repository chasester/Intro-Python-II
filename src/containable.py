from describable import *;
from container import *;
import utls;

class Containable:
    owner = None;
    def __init__(self, owner):
        if(type(self) is Useable): #stop from letting the user call this directly so you can never make a class that is purely Describable
            debugprint("This is a base class do not contruct here", True);
    def on_use(self):
        if(isDescribable()):
            print(f"{self.name} does nothing.");
        print("Has no effect");
        return true; #true means the item will be destroyed;

    def on_drop(self):
        if(isDescribable()):
            print(f"{self.name} has been dropped.");
        print("Dropped");

    def on_look(self, lit):
        return;
    
    def on_remove(self):
        if(isDescribable()):
            print(f"{self.name} has been removed.");
        print("Removed");
        return;

    def on_add(self, owner):
        if(owner is not None):
            owner.removeitem(self);
        if(not isinstance(owner, Container)):
            debugprint("Added Item to a container that doesnt exist", True);
            #object should be gc when object has no reference to owner.
            self.owner = None;
            #del self.owner;
        return;
    #debug code below
        if(isDescribable()):
            print(f"{self.name} has been added.");
        print("Added");
        return;

    def isDescribable(self):
        if(isinstance(self, Describable) or self.name is not ""): #name the object if we know the name
            return false;
        return true;
    def changeOwnership(self, owner):
        if(not isinstance(owner, Container)):
            print("Can not add to object that is not a container type.");
            raise;
        self.owner = owner;
        owner.add_item(self);
        
