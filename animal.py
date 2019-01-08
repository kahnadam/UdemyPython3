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
        Animal.__init__(self, name, species)
        self.breed = breed
        self.toy = toy

blue = Cat("Blue", "cat", "Scottish Fold", "string")
print(blue)
print(blue.species)
print(blue.breed)
print(blue.toy)
