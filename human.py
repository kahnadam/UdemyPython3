class Human:
    #let's say we want to keep "age" within logical bounds
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    """
    #without using properties, we can control how "age" is accessed like so:
    def get_age(self):
        return self._age

    #and change age with this method:
    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            self._age = 0
    """

    #now let's use properties!
    #even though we never set "age" as an attribute (we did _age), setting this property
    #means we can treat age like an attribute and call things like jane.age
    @property
    def age(self):
        return self._age

    #with this, we can now do things like jane.age = 20
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age can't be negative")

    #even though the age property is really a proxy for _age, which is used only internally,
    #setting the age property lets us access _age directly

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    #this isn't a good way to change full_name because you're changing two attributes at once
    #but it's an example to show it works, by splitting an input at the space:
    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")

jane = Human("Jane","Goodall",50)
#print(jane.get_age())
#jane.set_age(45)
#print(jane.get_age())
print(jane.age)
print(jane.full_name)
jane.full_name = "Joseph Schmoeseph"
print(jane.full_name)
print(jane.__dict__)
