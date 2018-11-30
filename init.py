class User:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

    #make a method to return first and last name
    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

user1 = User("Joe","Smith",68)
user2 = User("Biana","Lopez",31)

print(user2.full_name())
print(user1.initials())
