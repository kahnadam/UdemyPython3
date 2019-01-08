class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return "{} is a {}".format(self.name, self.species)

    def make_sound(self, sound):
        print("This animal says {}".format(sound))

class Cat(Animal):
    def __init__(self, name, species, breed, toy):
        self.name = name
        self.species = species
        self.breed = breed
        self.toy = toy

blue = Cat()
print(blue.make_sound("meow"))
