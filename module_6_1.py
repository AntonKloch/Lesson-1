from tkinter.font import names


class Animal:

    def __init__(self,name):
        self.name = name
        self.alive = True
        self.fed = False



    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:
    def __init__(self,name):
        self.name = name
        self.edible = False

class Mammal(Animal):
    def __init__(self,name):
        super(). __init__(name)

class Predator(Animal):
    def __init__ (self, name ):
        super(). __init__(name)

class Fruit(Plant):
    def __init__(self, name):
        super(). __init__(name)
        self.edible = True


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)




a1 = Predator("Лев")
a2 = Mammal("Корова")
p1 = Flower("Кактус")
p2 = Fruit("Банан")



print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
