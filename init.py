class User:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

    #make an instance method to return first and last name
    def full_name(self):
        return f"{self.first} {self.last}"

    #make an instance method to return initials
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    #make an instance method to return user liking a thing
    def likes(self,thing):
        return f"{self.first} likes {thing}"

user1 = User("Joe","Smith",68)
user2 = User("Biana","Lopez",31)

print(user2.full_name())
print(user1.initials())
print(user2.likes("ice cream"))
