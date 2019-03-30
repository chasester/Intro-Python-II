class Describable:
    name = "";
    description = ""; #full description of item
    adjectives = []; #adjectives used when defining this item #use when listing the item out in a menu

    def __init__(self, name, descption, adjectives):
        if(type(self) is Decribable): #stop from letting the user call this directly so you can never make a class that is purely Describable
            print("This is a base class do not contruct here");
            raise;
        self.name = toNameCase(str(name));
        self.desciption = str(description);
        self.adjectives = adjectives;#[str(i) for i in adjectives];

    def Decribe(self, chance=100):
        s = name;
        for i in adjectives:
            if(random.randint(min(chance,100),101)):
                s = i + " " + name;
        return s;

