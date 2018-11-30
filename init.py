class User:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

user1 = User("Joe","Smith",68)
user2 = User("Biana","Lopez",31)

print(user1.first, user1.last)
print(user2.first, user2.last)

class Animal:
    def __init__(self,name,legs,speed):
        self.name = name
        self.legs = legs
        self.speed = speed

tortoise = Animal("tortoise",4,"slow")
hare = Animal("hare",4,"fast")
print(tortoise.speed)
print(hare.speed)
