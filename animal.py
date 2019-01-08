class Animal:
    cool = True

    def make_sound(self, sound):
        print("This animal says {}".format(sound))

class Cat(Animal):
    pass

blue = Cat()
print(blue.make_sound("meow"))
