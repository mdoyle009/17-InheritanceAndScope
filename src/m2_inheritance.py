###############################################################################
# DONE: 1. (4 pts)
#
#   For this module, we are going to build off our Pet class that we created in
#   m2 of the session 16 coding exercises.
#
#   First, copy your completed version of your Pet class and paste it below
#   this _todo_.
#
#   Also, modify your speak() method to have a default response instead of the
#   barking we had before (feel free to be creative with this one).
#
#   The Pet class is going to be our parent class. That is, it will be the
#   class that our other classes inherit from.
#
#   Below, the Pet class, write a class called Dog that is a child class of
#   Pet.
#
#   This class should have a method called fetch() that prints:
#
#       "<Name of Dog> ran to get the stick!"
#
#   The Dog class should also have a speak() method that overrides the speak()
#   method of Pet. It should look the same as the one we had in session 16 with
#   the barking.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
class Pet:
    def __init__(about, name, age):
        about.name = name
        about.age = age
    def __str__(about):
        return f"Name: {about.name}, Age: {about.age}"
    def speak(about):
        print(f"{about.name} looks at you in silence.")

class Dog(Pet):
    def fetch(about):
        print(f"{about.name} ran to get the stick!")
    def speak(about):
        print(f"{about.name}: Bark! Bark! Bark!")

###############################################################################
# DONE: 2. (4 pts)
#
#   Now, write your own class of whatever type of pet you wish.
#
#   Your class should meet these criteria:
#
#       1. It should be a child class of Pet
#       2. It should have its own constructor with a name, age, and 2 more
#          attributes of your choosing.
#       3. It should also have two of its own methods (you can choose what
#          these methods do). They can be as simple as the ones we have done
#          before, but each one must use at least one of the attributes of your
#          pet.
#       4. Your pet should not have its own speak() method. It should just use
#          the default from the Pet class.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

class Bunny(Pet):
    def __init__(about, name, age, color, personality):
        about.name = name
        about.age = age
        about.color = color
        about.personality = personality
    def eat(about):
        if personality == "clumsy":
            print(f"{about.name} is so clumsy! It knocked over the food bowl!")
        if personality == "proper":
            print(f"Like a proper bunny, {about.name} gracefully ate the food.")
    def stare(about):
        print(f"{about.name} stares mindlessly at your bedroom wall. What is it thinking?")
    def groom(about):
        print(f"You softly groom {about.name}'s {about.color} fur.")

###############################################################################
# TODO: 3. (4 pts)
#
#   Now let's use our classes!
#
#   Write a method called main() that meets these criteria:
#
#       1. It should have at least two pets (a Dog and the pet you chose)
#       2. It should first print each pet using Pet's __str__ method
#       3. Each of your pets should use all of the methods that they are able
#          to use
#           
#           Dog
#               - speak()
#               - fetch()
#           Your own Pet
#               - speak()               <- using the one from the Pet class
#               - your own method x2
#
#   For step three, you can do them in any order you wish. You can even have
#   your pets interact with each other by alternating what they do.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def main():
    dog = Dog("Buster", 4)
    bunny = Bunny("Oscar", 7, "orange", "clumsy")
    print(dog)
    print(bunny)
main()
