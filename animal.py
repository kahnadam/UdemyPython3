class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return "{} is a {}".format(self.name, self.species)

    def make_sound(self, sound):
        print("This animal says {}".format(sound))

#you can use super() to init Cat as child of Animal, which runs Animal.__init__
#and passes in self as the first argument
class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} likes to play with {self.toy}")

blue = Cat("Blue", "Scottish Fold", "string")
print(blue)
print(blue.species)
print(blue.breed)
print(blue.toy)
print(blue.play())
