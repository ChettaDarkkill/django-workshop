#class
"""
class Dog:

    dogInfo = "Hey dogs are cool"

    def bark(self, str):
        print("BARK!" + str)

mydog = Dog()
mydog.bark("hello")
mydog.name = "Fido"
mydog.age = 16
print(mydog.name)
print(mydog.age)

print(Dog.dogInfo)


class Dog:

    def __init__(self, name, age, forcolor):
        self.name = name
        self.age = age
        self.forcolor = forcolor

    def bark(self, str):
        print("BARK!" + str + self.forcolor)

mydog = Dog("Fido", 13, "Brow")
print(mydog.age)
mydog.bark("Hello")
"""

#Dictionaries

"""
dogs = {"Fido":8, "Sally":17, "Sean":2}
del(dogs["Fido"])
print(dogs)
"""

#loop
dognames = ["Fido", "Sean", "Sally", "Mark"]
"""
for dog in dognames:
    print(dog)
    for x in range(1,1):
    print(x)

    age = 0
while age < 18:
    print(age)
    age += 1
"""

#list
dognames = ["Fido", "Sean", "Sally", "Mark", 4234, False, True, 4.23]
"""dognames.insert(0, "Jane")
#del(dognames[2])
print(len(dognames))
dognames[1] = "Jane"
print(dognames)
"""



#function
"""
age = 17

name = "Matt"

todayIsCold = False


def hello(name, age):
    return "Hello {} you are {} years old".format(name, age)

sentence = hello("Mark", 17)
print(sentence)
"""

# test comment
# test comment

""" test """
"""
if age != 14:
    print("You are older than 18")
    print("This is another line")
else:
    print("you are younger than 18")
"""