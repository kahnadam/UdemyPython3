class User:
    active_users = 0


    #- @classmethod is a decorator to indicate this function is a class method
    #- naming this cls instead of self is a way of indicating to the programmer
    #that this function refers to the class, not the instance

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    #create a classmethod that converts a string into variables that can be
    #used to make a new object. Split the string along commas and assign
    #to the variables
    @classmethod
    def from_string(cls,data_string):
        first, last, age = data_string.split(",")
        return cls(first,last,int(age))

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

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

#user1 = User("Joe","Smith",68)
#user2 = User("Bianca","Lopez",31)
#print(User.display_active_users())
#user3 = User("Tom","Franco",22)
#user4 = User("Marie","Ford",66)
#print(User.display_active_users())

tom = User.from_string("Tom,Jones,89")
print(tom.first)
print(tom.full_name())
print(tom.birthday())
