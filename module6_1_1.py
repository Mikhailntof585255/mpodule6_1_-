class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = food
        if food.eduble == True:
            print(f"{self.name} съел {food.food} ")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.food}")
            self.alive = False


class Plant:
    eduble = False

    def __init__(self, food):
        self.food = food


class Flower(Plant):
    pass


class Fruit(Plant):
    eduble = True
    pass


class Predator(Animal):
    pass


class Mammal(Animal):
    pass


a1 = Predator("Волк с Уолл_Стрит")
a2 = Mammal("Хатико")
p1 = Flower("Цветик семицветик")
p2 = Fruit("Заводной апельсин")
print(a1.name)
print(a2.name)
print(p1.food)
print(p2.food)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
