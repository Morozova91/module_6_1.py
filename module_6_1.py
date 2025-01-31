# "Зачем нужно наследование"
# Задача "Съедобное, несъедобное":
# У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(food) - метод, где food - это параметр, принимающий объекты классов растений.
#
# Метод eat должен работать следующим образом:
# Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
# Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
# Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.
#
# У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
#
class Animal:
    alive = True  #(живой)
    fed = False  #(накормленный)

    def __init__(self, name):
        self.food = Plant
        self.name = name


class Mammal(Animal):
    alive = True

    def eat(self, food):
        self.food = Plant
        if food is Fruit(Plant):
            print(self.name, 'съел', food.name)
            fed = True
        else:
            print(self.name + 'не стал есть,' + food.name)
            alive = False


class Predator(Animal):
    alive = True

    def eat(self, food):
        self.food = Plant
        if food is Plant:
            print(self.name + 'не стал есть' + food.name)
            alive = False


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    edible = False
    pass


class Fruit(Plant):
    edible = True
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)