class Animal:
    def __init__(self, name, type, FoodType):
        self.name = name
        self.type = type
        self.FoodType = FoodType
    
    def printDescription(self):
        print(self.name + " is a type of " + self.type + " and has a type of food " + self.FoodType)

    def eat(self, food):
        print(self.name + " is eating " + food)

    def sleep(self):
        print(self.name + " is sleeping")

class Chicken(Animal):
    def sound(self):
        print(self.name + " : " + "Cook-a-doodle-doo!")

class Sheep(Animal):
    def sound(self):
        print(self.name + " : " + "baa.. baa..")

Chicken1 = Animal("Chicken1", "Aves", "Omnivores")
Sheep1 = Animal("Sheep1", "Mammal", "Herbivores")

Chicken1.printDescription()
Chicken1.sleep()
Chicken1.eat("grains")

Sheep1.printDescription()
Sheep1.sleep()
Sheep1.eat("grass")

Chicken2 = Chicken("Chicken2", "Aves", "Omnivores")
Chicken2.sound();

Sheep2 = Sheep("Sheep2", "Mammal", "Herbivores")
Sheep2.sound();
# Chicken2.printDescription()
# Chicken2.sleep()
# Chicken2.eat("grains") 
