from containable import *;
import utls;
class Container:
    items = [];
    def __init__(self):
        if(type(self) is Useable): #stop from letting the user call this directly so you can never make a class that is purely Describable
            debugprint("This is a base class do not contruct here", True);

    def add_item(self,item):
        if(not isinstance(item, Containable)): return;
        try: #make sure item isnt already in list so we cont double spawn items
            items.remove(item);
        except: #this is the defult path.
            pass;
        items.append(item);
        item.on_add(self);

    def add_items(self, arr):
        for i in arr: self.add_item(i);

    def remove_item(self, item, parr):
        try:
            items.remove(item);
            item.on_remove();
        except:
            pass; #comes here if item is not in list

    def remove_items(self, arr):
        for i in arr: self.removeitem(i);
    
    def use_item(self, item):
        try:
            if(item.on_use()):
                self.removeitem(item);
        except:
            pass; #item does not exist or is not useable (ie its not containable)
