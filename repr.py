class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls,data_string):
        first, last, age = data_string.split(",")
        return cls(first,last,int(age))

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    #without this method, if you do something like print an object
    #e.g., print(tom)
    #you get just a bunch of python code like "<__main__.User object at 0x107085390>"
    #so this changes how an object is represented
    def __repr__(self):
        return f"{self.first} is {self.age}"

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self,thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age} birthday, {self.first}"

tom = User.from_string("Tom,Jones,89")
print(tom)

j = User("Judy","Steele",18)
print(j)
