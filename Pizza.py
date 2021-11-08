class Pizza:
    def __init__(self, pizzaName, topping):
        self.pizzaName = pizzaName
        self.topping = topping
    
    def printNameAndTopping(self):
        print(self.pizzaName + " has a topping ", end = "")
        i = 0
        for x in self.topping:
            if i != 0:
                print(", ", end = "")
            print(x, end = "")
            i += 1
        print()

topping1 = ["Mozzarella", "Cheese"]
Pizza1 = Pizza("Pizza 1", topping1)
topping2 = ["Beef", "Mushroom", "Cheese"]
Pizza2 = Pizza("Pizza 2", topping2)

Pizza1.printNameAndTopping()
Pizza2.printNameAndTopping()