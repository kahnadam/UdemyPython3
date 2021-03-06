class User:
    #define a class attribute called active_users
    active_users = 0

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        #whenever a new user is initialized, increase active_users by one
        #this is User. instead of self. because it's a class attribute
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    #make an instance method to return first and last name
    def full_name(self):
        return f"{self.first} {self.last}"

    #make an instance method to return initials
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    #make an instance method to return user liking a thing
    def likes(self,thing):
        return f"{self.first} likes {thing}"

    #boolean method to check if object is a senior citizen
    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age} birthday, {self.first}"

#instantiate two objects
user1 = User("Joe","Smith",68)
user2 = User("Bianca","Lopez",31)

print(user2.full_name())
print(user1.initials())

#for the likes method you need to pass in a thing
print(user2.likes("ice cream"))

#is_senior is a boolean method to see if user is a is_senior
print(user1.is_senior())
print(user2.is_senior())

#age
print(user1.age)
print(user1.birthday())
print(user1.age)
